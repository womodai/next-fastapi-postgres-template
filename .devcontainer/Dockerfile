# ベースは公式のPythonイメージ（Slimで軽量）
FROM mcr.microsoft.com/devcontainers/python:3.11

# Node.js（Next.js用）をインストール
ARG NODE_VERSION=20
RUN curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash - \
    && apt-get update \
    && apt-get install -y nodejs

# 最新のnpmとpnpmをインストール（任意でYarnでも可）
RUN npm install -g npm@latest pnpm

# PostgreSQLクライアントも入れておくと便利（psqlなど）
RUN apt-get install -y postgresql-client

# 作業ディレクトリ（マウント先）を設定
WORKDIR /workspace

# 推奨：pipのキャッシュを使ってvenv作成時のパフォーマンスを向上
ENV PIP_NO_CACHE_DIR=off \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# エイリアスなどの共通設定（必要に応じて追加）
RUN echo 'alias ll="ls -alF"' >> ~/.bashrc