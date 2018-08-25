from django.shortcuts import render
from templateapp.person import Person

# 传递给模版的是字典
def dict_info(request):
    mydict = {"name":"tom","age":20,"sex":"男"}
    return render(request,'mytemplate/templatedemo.html',{"dictinfo":mydict})

# 传递给模版的是对象
def object_info(request):
    per = Person("alice",25,"女")
    return render(request,'mytemplate/templatedemo.html',{"objinfo":per})

# 传递给模版的是列表
def list_info(request):
    fruits = ["苹果","香蕉","橘子","西瓜"]
    return render(request,'mytemplate/templatedemo.html',{'listinfo':fruits})


def iftag(request):
    athletes = ["乔丹","姚明","卡卡"]
    coachs = []
    return render(request,'mytemplate/iftag.html',{"athlete_list":athletes,"coach_list":coachs})

def fortag(request):
    books = ["三国演义","红楼梦","水浒传","西游记"]
    links = ["百度","搜狐","阿里巴巴","谷歌"]
    fruits = []
    return render(request,'mytemplate/fortag.html',{'book_list':books,"company_list":links,"fruit_list":fruits})



