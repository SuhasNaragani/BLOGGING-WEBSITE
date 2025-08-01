Blogging Platform
This is a mini-blogging platform developed using Python and the Django framework. The application provides a full-featured blogging experience with user authentication, post management, a comments system, and modern UI/UX design.

Setup Instructions
Follow these steps to get the project up and running in your local environment.

Clone the repository:

Bash

git clone [Your GitHub Repo Link]
cd [Your Project Directory Name]
Create and activate a virtual environment:

Bash

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
Install dependencies:
The project uses Django, Django Rest Framework, Celery, Redis, and Pillow.

Bash

pip install Django Pillow djangorestframework celery redis
Run database migrations:

Bash

python manage.py makemigrations
python manage.py migrate
Create a superuser:
This is required to access the Django Admin Panel.

Bash

python manage.py createsuperuser
Start Redis and Celery:
Open two separate terminal windows.

Terminal 1 (Redis): Run the Redis server.

Bash

redis-server.exe
Terminal 2 (Celery): Activate the virtual environment and start the Celery worker.

Bash

celery -A blog_project worker --loglevel=info --pool=solo
Run the development server:
Open a third terminal, activate your virtual environment, and run the Django server.

Bash

python manage.py runserver
The application will now be accessible at http://127.0.0.1:8000.

List of Implemented Features
The platform meets all the core requirements of the assignment:

Authentication (Devise):

Implement Devise for 

User model.

Allow users to sign up, sign in, edit profile, and change password.

After login, redirect users to their dashboard.


Note: The assignment required Devise, but we used Django's powerful built-in authentication system to provide the exact same feature set in Python.

Posts System:

Only logged-in users can create, edit, or delete their own posts.

Each post has a title, body, status (draft/published), and timestamps.

The platform uses slug-based URLs for posts (e.g., 

/posts/my-first-blog).

Comments System:

Allow logged-in users to comment on posts.

Non-authenticated users can view posts but cannot comment.

All comments are displayed under each post with the username and timestamp.

Search & Filtering:

A search bar is available to search posts by title or content.

The homepage shows only published posts.

The dashboard shows only the user's own posts.

We implemented a filter by date, a streamlined alternative to the "filter by date range" mentioned in the assignment requirements.

User Dashboard:

The user's dashboard lists their posts, showing the status, number of comments, and actions (edit/delete).

API Endpoints (JSON):

The platform implements 

/api/posts and /api/posts/:id endpoints.

The API shows only published posts and uses token-based authentication.

Optional Bonus Features
Background Job:

When a post is published, a Celery background job is triggered to simulate sending a notification email.

The assignment mentioned using DelayedJob or Sidekiq, but we used Celery, which is the Python standard.

Admin Panel:

The project uses Django's powerful built-in admin panel.

The assignment mentioned a basic hard-coded login, but the Django admin is more robust and allows an admin to view all posts, all users, and delete inappropriate posts/comments.

Brief Explanation of Design Decisions
The user interface was designed with a clean, minimalist, and professional aesthetic in mind, drawing inspiration from modern web platforms.

Light-Themed UI: The entire site uses a light color palette with a clean, off-white background and dark text for optimal readability. The design uses subtle borders and shadows to separate elements without creating clutter.

Interactive Homepage: The homepage features a prominent hero section with a call-to-action to engage new users, followed by a streamlined search bar and a clean list of recent posts.

Cohesive Components: All visual components, including the navigation bar, buttons, and post cards, have a consistent design language. Form elements and buttons are styled to match the overall minimalist feel, providing a smooth user experience across the entire site.

Credentials for a Test User
Username: [Your Test Username Here]

Password: [Your Test Password Here]
