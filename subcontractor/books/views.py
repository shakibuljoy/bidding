from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Book
from .forms import BookForm, BookFormSet


def create_book(request, pk):
    author = Author.objects.get(pk=pk)
    form = BookForm(request.POST or None)
    book = Book.objects.filter(author=author)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            print("Redirected")
            return redirect('detail-book', pk=book.id)
            
        else:
            context = {
                'form':form
            }
            return render(request, "partials/create_book_form.html")

    context = {
        'form': form,
        'author':author,
        'books': book
    }
    return render(request, "create_book.html", context)


def create_book_form(request):
    context = {
        'form': BookForm()
    }
    return render(request, "partials/create_book_form.html", context)


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)
    context = {
        'form': form,
        'book': book
    }
    if request.method == 'POST':
        if form.is_valid():
            book = form.save()
            return redirect('detail-book', pk=book.id)
            
        else:
            context = {
                'form':form
            }
            return render(request, "partials/create_book_form.html")
    return render(request, "partials/create_book_form.html", context)


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book':book
    }
    return render(request, 'partials/book_detail.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse()