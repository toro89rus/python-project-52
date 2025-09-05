# Task manager

## Hexlet tests, SonarQube, linter statuses

[![Actions Status](https://github.com/toro89rus/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/toro89rus/python-project-52/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=toro89rus_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=toro89rus_python-project-52)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

### Description

Task Management application built with Django.
It provides user authentication and role-based access to core features such as managing tasks, statuses, and labels.

### Features

- User authentication and personal profile management
- Full CRUD for tasks, statuses, and labels
- Task filtering by status, executor, label, or author
- Data integrity: linked users, statuses, or labels cannot be deleted
- Internationalization (English and Russian)
- Error tracking integration with Rollbar

### Requirements

- `Python 3.12`
- `uv`
- `make`
- `SQLite(default)/PostgreSQL(production)`

### Installation

#### Step 1: Clone the Repository

```bash
git clone https://github.com/toro89rus/python-project-52.git
cd python-project-52
make install
```

#### Step 2: Apply Migrations

```bash
make migrate
```

SQLite will be used by default in development.
For PostgreSQL, provide DATABASE_URL in .env.

#### Step 3: Configure environment variables

Create a .env file

```bash
# .env
SECRET_KEY=some_secret
DATABASE_URL=postgres://user:password@host:port/database_name
ROLLBAR_TOKEN=your_rollbar_token
IS_PRODUCTION=true # toggle production/development mode
ALLOWED_HOSTS=localhost,127.0.0.1 # allowed hosts is set to localhost and 127.0.0.1 for development mode by default, for production you need to set host manually
```

#### Step 4: Run the Application

```bash
make start
```

The application should be accessible at <http://127.0.0.1:8000>.

Check live demo on [Render.com](https://task-manager-2c0i.onrender.com/) (Due to render policy, free instance may spin down with inactivity, which can delay requests by 50 seconds or more.)
