# Django Blog Application

This repository contains a simple blogging web application built using Django, where users can create accounts, write blog posts, and view blog posts from other authors. The application comes with features like user authentication, blog creation, blog updates, and blog deletion.

## Installation

1. Clone the repository to your local machine:
```
git clone https://github.com/your-username/django-blog.git
cd django-blog
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Apply the database migrations:
```
python manage.py migrate
```
4. Create a superuser to access the Django Admin interface:
```
python manage.py createsuperuser
```
5. Start the development server:
```
python manage.py runserver
```
## Usage
1. Access the application in your web browser at http://localhost:8000/.

2. Create an account using the Sign Up page and become an author to write blog posts.

3. After signing up, you can log in using the Login page and access your dashboard.

4. On your dashboard, you can view, add, update, and delete your blog posts.

## Contributing
Contributions are welcome! If you find any issues or have ideas for improvements, please submit a pull request or create an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.