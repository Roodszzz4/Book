
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('all_books', views.all_books, name='all_books'),
    path('all_authors', views.all_authors, name='all_authors'),
    path('more/<int:pk>', views.more, name='more'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_book/', views.add_book, name='add_book'),

    ]

