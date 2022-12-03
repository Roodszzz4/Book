from django.contrib import admin
from .models import Book, Author, Genre


class BookInLine(admin.TabularInline):
    model = Book
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_id', 'year_of_issue', 'publishing_house', 'genre_display', 'language']
    filter_horizontal = ['genre',]
    # search_fields???


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo',]
    inlines = [BookInLine, ]


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ['title',]
