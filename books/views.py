from django.shortcuts import render, get_object_or_404

from books.models import Book, Author


def index(request):
    return render(request, 'base.html')


def all_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'all_books.html', context=context)

def all_authors(requvest):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(requvest, 'all_authors.html', context=context)

def more(request, pk):
    authors = get_object_or_404(Author, pk=pk)
    return render(request, 'more.html', context={'authors': authors})