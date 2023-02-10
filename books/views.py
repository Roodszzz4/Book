from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from books.forms import AuthorForm, BookForm
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


@login_required
def add_author(request):
    form = AuthorForm
    context = {
        'form': form

    }
    if not request.user.is_superuser:
        if request.method == 'POST':
            form = AuthorForm(request.POST, request.FILES)
        else:
            return HttpResponse('You are do not superuser status')
        if form.is_valid():
            author = Author.objects.create(**form.cleaned_data)

            return HttpResponse(f'Author {author} is add')

    return render(request, 'author_form.html', context=context)

@login_required
def add_book(request):
    form = BookForm
    context = {
        'form': form
    }
    if not request.user.is_superuser:
        if request.method == "POST":
            form = BookForm(request.POST, request.FILES)
        else:
            return HttpResponse('You are do not superuser status')
        if form.is_valid():
            book = Book.objects.create(**form.cleaned_data)
            return HttpResponse(f'Book {book} is add')
    return render(request, 'book_form.html', context=context)

def del_authors(request, id):
    authors = get_object_or_404(Author, id=id)
    authors.delete()
    return redirect(reverse_lazy('all_authors'))

def del_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect(reverse_lazy('all_books'))

