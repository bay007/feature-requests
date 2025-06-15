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

## Administration

Access the admin interface at http://127.0.0.1:8000/admin/ to manage features, votes, and comments.
