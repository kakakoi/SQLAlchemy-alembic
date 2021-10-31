# SQLAlchemy-alembic-migration

# Installation

```bash
pip install --upgrade pip
pip install psycopg2
pip3 install alembic sqlalchemy
alembic init alembic_sample

```

# Usage

user.pyを編集して下記を実行
```bash
alembic revision --autogenerate -m "create tables"
alembic upgrade head
```
