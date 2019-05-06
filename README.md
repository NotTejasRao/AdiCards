# LeetCards
_A flashcard web application created in Python using Django._

## Screenshots

### Homepage
![homepage.png](docs/homepage.png?raw=true)

### Adding Flashcards to Multiple Decks
![one_to_many.png](docs/one_to_many.png?raw=true)
![decks_example.png](docs/decks_example.png?raw=true)


## Installation
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

Migrate models to the database:
```
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

Run the development server:
```
python manage.py runserver
```

You should now have the project running on localhost:8000.

## Contribute

Care to make this project better? Follow these conventions and submit a pull request!

1. Use "from file.py import ClassName" for classes, and "import path.to.file.py as file" to reference definations.
2. Prefix html files with the object they interact with (ex. flashcard) and suffix with what it helps do to them (ex. create) -- ie. flashcard_create.html is acceptable.

## Licence
GPL2
