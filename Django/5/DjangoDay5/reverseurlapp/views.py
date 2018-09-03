from django.http import HttpResponseRedirect
from django.shortcuts import render
from reverseurlapp.models import *

def show_books(request):
    books = Book.objects.all()
    return render(request,'book/allbooks.html',locals())

def detail_book(request,bid):
    book = Book.objects.get(id=bid)
    return render(request,'book/detail.html',locals())


def update_book(request):
    bid = request.POST.get("bookId")
    book = Book.objects.get(id=bid)   # 先根据id获取对象,该对象与表中的记录对应
    book.name = request.POST.get("bookName")
    book.author = request.POST.get("bookAuthor")
    book.price = request.POST.get("bookPrice")
    book.save()  # 保存修改
    return HttpResponseRedirect('/reverse/all/')
