from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from books.models import Book


def index(request):
    return redirect('books_list')


def shows_books_list(request):
    template = 'books/books_list.html'
    context = {
        'books': [entry for entry in Book.objects.order_by('author')],
        'has_prev_next_navigation': False
    }
    return render(request, template, context)


def shows_books_list_pub_date(request, pub_date):
    template = 'books/books_list.html'
    
    try:
        prev_pub_date = Book.objects.filter(pub_date__lt=pub_date).latest('pub_date').pub_date
    except ObjectDoesNotExist:
        prev_pub_date = None

    try:
        next_pub_date = Book.objects.filter(pub_date__gt=pub_date).earliest('pub_date').pub_date
    except ObjectDoesNotExist:
        next_pub_date = None
        
    context = {
        'books': [entry for entry in Book.objects.filter(pub_date=pub_date)],
        'has_prev_next_navigation': True,
        'prev_pub_date': prev_pub_date,
        'next_pub_date': next_pub_date
    }
    return render(request, template, context)
