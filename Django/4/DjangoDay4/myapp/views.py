from django.http import HttpResponseRedirect
from django.shortcuts import render
from myapp.models import Country

def go_country(request):
    return render(request,'myapptemplate/add.html')

# 添加国家
def add_country(request):
    country_name = request.POST.get("countryName")  # 接收国家名称
    country_capital = request.POST.get("capital")
    country_king = request.POST.get("king")
    # 添加数据到数据库，并返回新添加的模型对象
    new_country = Country.objects.create(name=country_name,capital=country_capital,king=country_king)
    return HttpResponseRedirect("/myapp/showall/")

# 展示所有国家
def show_all(request):
    country_set = Country.objects.all()
    return render(request,'myapptemplate/showall.html',locals())

# 通过国家的id删除对应国家
def delete_byid(request,country_id):
    Country.objects.get(id=country_id).delete()  # 删除对应的模型对象
    return HttpResponseRedirect("/myapp/showall/")
