LeetCards
======
A flashcard web app created in Python using Django.

Installation:
-----------
Create a Django project:
```
django-admin startproject mysite
```

Clone this repository in the root directory of that project:
```
git clone https://github.com/NotTejasRao/LeetCards.git
```

In ```urls.py```, add:
```python
urlpatterns = [path('', include('leetcards.urls'))]
```

In ```settings.py```, add:
```python
INSTALLED_APPS = ['leetcards']
```

Create the database:
```
python manage.py migrate
```

Run the development server:
```
python manage.py runserver
```

You should now have the project running on localhost:8000

Coding Conventions:
-----------

1. Use "from file.py import ClassName" for classes, and "import path.to.file.py as file" to reference definations.
2. Prefix html files with the object they interact with (ex. flashcard) and suffix with what it helps do to them (ex. create) -- ie. flashcard_create.html is acceptable.

Licence:
-----------
GPL2
