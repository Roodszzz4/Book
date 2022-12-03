from django.contrib import admin
from .models import Book, Author, Genre


class BookInLine(admin.TabularInline):
    model = Book
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_id', 'amount_page', 'year_of_issue', 'publishing_house', 'genre_display', 'language', ]
    filter_horizontal = ['genre', ]
    # search_fields???





@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'count_book', 'short_add', 'title_book', 'sum_pages',]
    inlines = [BookInLine, ]

    def count_book(self, obj):
        return obj.books.count()

    def short_add(self, obj):
        bio = obj.biography.split()
        bio = bio[:10]
        return f"{' '.join(bio)}..."

    def sum_pages(self, obj):
        return sum(i.amount_page for i in obj.books.all())




    def title_book(self, obj):
        return '; '.join([i.title for i in obj.books.all()])















@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ['title', ]
