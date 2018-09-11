from django.http import HttpResponse, Http404
from django.shortcuts import render

# 引发500错误
def compute(request):
    a = 100 / 0
    return HttpResponse("ok")

# 引发404错误
def go_wrong(request):
    print("进入go_wrong()视图")
    return render(request,'nopage.html')


def my500(request):
    return render(request,'error/500.html')

def my404(request):
    return render(request,'error/404.html')
