from django.http import HttpResponse
from django.shortcuts import render
from formapp.forms import MilkForm


def milk_form(request):
    if request.method == "POST":
        mf = MilkForm(request.POST)
        if mf.is_valid():   # 当验证通过
            milkname = mf.cleaned_data["name"]   # 从表单对象中提取数据
            milkprice = mf.cleaned_data["price"]
            return render(request,'success.html',locals())
    else:
        mf = MilkForm()
        return render(request,'milk.html',{'myform':mf})


