from django.shortcuts import render

def go_link(request):
    return render(request,'homework/link.html')

def show_hobby(request):
    your_hobby = request.GET.get("hobby")
    print("你的爱好是："+your_hobby)
    return render(request,'homework/hobby.html',{'love':your_hobby})

def show_author(request,author,price):
    print("接收到的作者是："+author+"；价格是："+price)
    return render(request,'capture/book.html',{'book_author':author,'book_price':price})

def convert(request,a,b):
    result = a + b
    return render(request,'capture/convert.html',{"result":result})

def hello(request):
    return render(request,'hello.html')
