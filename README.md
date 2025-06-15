# Feature Request System

A Django-based web application for collecting and managing feature requests anonymously.

## Features

- Anonymous feature request submissions without login
- Feature listing with voting capability
- Vote tracking using cookies to prevent duplicate votes
- Comment system for each feature request
- Responsive design with Tailwind CSS 4

## Technical Stack

- Django 5.2
- SQLite database
- Tailwind CSS 4 (via CDN)
- MVC architecture with Django templates

## Requirements

- Python 3.8 or higher
- Django 5.2.3

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd feature-request
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Apply migrations:
```bash
python manage.py migrate
```

4. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Access the application at http://127.0.0.1:8000/

## Usage

- **View Features**: Navigate to the homepage to see all submitted feature requests
- **Submit Features**: Fill out the form on the homepage or go to the dedicated submission page
- **Vote on Features**: Click the thumbs-up icon to vote (or remove your vote)
- **Comment on Features**: Click on a feature to view details and add comments

## Administration

Access the admin interface at http://127.0.0.1:8000/admin/ to manage features, votes, and comments.
