from django.shortcuts import render
import datetime

def go_xian(request):
    return render(request,'mytemplate/child.html')

def show_filter(request):
    fruit_info = "strawberry is My FAvoRiTE fruit"
    d = datetime.datetime(2018,8,8)
    return render(request,'mytemplate/filter.html',{'fruit':fruit_info,'date_info':d})

def use_locals(request):
    country = "中国"
    color = "苹果"
    capital = "北京"
    school = "清华大学"
    return render(request,'mytemplate/local.html',locals())
