
# ApplyTrack – Job Application Tracking System

ApplyTrack is a web-based job application tracking system developed using Python and Django. It helps users organize, monitor, and manage their job applications through a centralized dashboard.

## Features

- Add new job applications
- View all job applications
- Edit application details
- Delete job applications
- Search applications by company name or job title
- Track application status
- Dashboard overview
- Light and dark mode

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript
- Git and GitHub

## Application Status

- Applied
- Assessment
- Interview
- Selected
- Rejected

## Project Structure

ApplyTrack/
│
├── applications/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── README.md

## Installation and Setup

1. Clone the repository:

   git clone https://github.com/yaasethanandhakumar/ApplyTrack.git

2. Navigate to the project directory:

   cd ApplyTrack

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   Windows:
   venv\Scripts\activate

5. Install Django:

   pip install django

6. Apply database migrations:

   python manage.py migrate

7. Start the development server:

   python manage.py runserver

8. Open your browser:

   http://127.0.0.1:8000/

## Future Improvements

- Application status analytics
- Visual dashboard charts
- Additional application insights

## Author

Yaasetha N
