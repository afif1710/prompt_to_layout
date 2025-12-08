# AI UI Builder Backend

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure database:
```bash
# Create database
mysql -u root -p
> CREATE DATABASE ai_ui_builder;
> exit;

# Copy environment file
cp .env.example .env
# Edit .env with your database credentials
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run server:
```bash
python manage.py runserver
```

Server: http://127.0.0.1:8000
