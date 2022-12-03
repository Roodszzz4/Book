from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='image/')
    biography = models.TextField(default='')

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title


book_language = [
    ('EN', 'English'),
    ('UA', 'Ukraine'),
    ('PL', 'Poland',)
]


class Book(models.Model):
    title = models.CharField(max_length=55)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    year_of_issue = models.DateField('date published')
    publishing_house = models.CharField(max_length=50)
    language = models.TextField(choices=book_language)
    genre = models.ManyToManyField(Genre, related_name='books')

    def genre_display(self):
        return '. '.join([genre.title for genre in self.genre.all()])

    genre_display.short_description = 'Genre'

    def __str__(self):
        return self.title
