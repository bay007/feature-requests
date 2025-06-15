# Feature Request System

A Django-based web application for collecting and managing feature requests anonymously.

## Features

- Anonymous feature request submissions without login
- Feature listing with voting capability
- Vote tracking using cookies to prevent duplicate votes
- Comment system for each feature request
- Responsive design with Tailwind CSS 4
- UUID-based primary keys for enhanced security and scalability
- PostgreSQL database support

## Technical Stack

- Django 5.2
- PostgreSQL database
- Tailwind CSS 4 (via CDN)
- MVC architecture with Django templates

## Requirements

- Python 3.8 or higher
- Django 5.2.3
- PostgreSQL 12 or higher
- psycopg2-binary 2.8.4

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd feature-request
```

2. Set up environment variables:

For development:
- Copy `.env.dev.example` to `.env.dev`
- Edit `.env.dev` with your development database credentials
```bash
cp .env.dev.example .env.dev
# Edit .env.dev with your database settings
```

For production:
- Set environment variables directly in your system/deployment platform
- Required variables:
  - DJANGO_ENV=production
  - POSTGRES_DB
  - POSTGRES_USER
  - POSTGRES_PASSWORD
  - POSTGRES_HOST
  - POSTGRES_PORT
  - ALLOWED_HOSTS (comma-separated list of allowed domains, e.g. 'features.aiba.mx,localhost')

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application at http://127.0.0.1:8000/

## Database Configuration

### Development
The application uses PostgreSQL in both development and production. In development:
- Configuration is read from `.env.dev`
- Default host is localhost
- Default port is 5432

### Production
In production:
- Set `DJANGO_ENV=production`
- All database configuration must be provided through environment variables
- No configuration files are read for security
- Required variables: POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT

## Model Structure

All models use UUID fields as primary keys for enhanced security and scalability:
- Feature model: UUID-based ID with title, description, and timestamps
- Vote model: UUID-based ID linking to features
- All tables include created_at and updated_at timestamps

## Usage

- **View Features**: Navigate to the homepage to see all submitted feature requests
- **Submit Features**: Fill out the form on the homepage or go to the dedicated submission page
- **Vote on Features**: Click the thumbs-up icon to vote (or remove your vote)
- **Comment on Features**: Click on a feature to view details and add comments

## Docker Compose Setup

### Prerequisites
- Docker
- Docker Compose

### Running with Docker Compose

1. Create a `docker-compose.yml` file in the project root:
```yaml
version: '3.8'
services:
  db:
    image: postgres:14
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_PORT: ${POSTGRES_PORT:-5432}
      ALLOWED_HOSTS: ${ALLOWED_HOSTS:-localhost}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 5s
      timeout: 5s
      retries: 5

  web:
    build: .
    command: >
      sh -c "python manage.py migrate &&
             python manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    env_file:
      - .env.dev
    depends_on:
      db:
        condition: service_healthy

volumes:
  postgres_data:
```

2. Set up your environment variables:
```bash
cp .env.dev.example .env.dev
# Edit .env.dev with your database settings
# Make sure POSTGRES_HOST=db in .env.dev to match the service name
```

3. Build and start the services:
```bash
docker compose up --build
```

4. Create a superuser (in a new terminal):
```bash
docker compose exec web python manage.py createsuperuser
```

5. Access the application at http://localhost:8000/

To stop the services:
```bash
docker compose down
```

To stop the services and remove all data (including database):
```bash
docker compose down -v
```

## Administration

Access the admin interface at http://127.0.0.1:8000/adminkarmp2/ to manage features, votes, and comments.
