# Next.js + FastAPI + PostgreSQL Template (Dockerized Fullstack Dev Env)

このリポジトリは、**Next.js (React 19 + Tailwind CSS v4)** フロントエンドと  
**FastAPI + PostgreSQL** バックエンドの**フルスタック開発環境**を  
**Docker + devcontainer + WSL2** 上に構築するためのテンプレートです。

## 📦 技術スタック

| 分類             | 技術                            |
|------------------|---------------------------------|
| フロントエンド   | Next.js 14 (React 19, App Router) + Tailwind CSS v4 |
| バックエンド     | FastAPI (Python 3.11)            |
| データベース     | PostgreSQL 15                    |
| 開発環境         | Docker, Docker Compose, WSL2, DevContainer |
| バージョン管理   | GitHub（SSH認証対応済）          |

---

## 🏁 セットアップ手順（VS Code DevContainer 使用）

### 1. 前提条件
- Docker Desktop がインストールされていること
- WSL2 有効化済み（Linuxディストリビューションがセットアップ済み）
- VS Code + Dev Containers 拡張機能がインストールされていること

### 2. このリポジトリをクローン

```bash
git clone git@github.com:YOUR_USERNAME/next-fastapi-postgres-template.git
cd next-fastapi-postgres-template
```
### 3. Dev Container を起動（初回ビルド）
VS Code でこのフォルダを開き、Reopen in Container を選択。

### 4. 自動初期化コマンド（postCreateCommand により）
```bash
cd frontend && npm install
cd ../backend && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

### 🌐 フロントエンド（Next.js）
```bash
cd frontend
npm run dev
# http://localhost:3000 で開発サーバーが起動
```

### 🔧 バックエンド（FastAPI）
```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
# http://localhost:8000/docs でAPIドキュメント（Swagger）を確認
```

### 🗂️ ディレクトリ構成
```plaintext
.
├── frontend/        # Next.js + Tailwind CSS
├── backend/         # FastAPI アプリ
├── .devcontainer/   # VS Code Dev Container 設定
├── docker-compose.yml
├── README.md
└── .gitignore
```

### 🔐 環境変数ファイル（例）
frontend/.env.local
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

backend/.env
```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_pass
POSTGRES_DB=your_db
DATABASE_URL=postgresql://your_user:your_pass@db:5432/your_db
```

### 📄 ライセンス
MIT License

### 🧭 今後の拡張予定（任意で記述）
- ユーザー認証（JWT or OAuth2）

- CI/CD（GitHub Actions）

- Prisma や SQLAlchemy を用いたORMの強化

- Cloudflare R2 や外部ストレージ連携