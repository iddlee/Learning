from django.shortcuts import render

def show_fruits(request):
    fruits = ["菠萝","西瓜","香蕉","苹果"]
    return render(request,'homework/fruits.html',{"fruit_list":fruits})

def sports(request,tag):
    sport_list = []
    if tag == "allsports":
        sport_list = ["足球","篮球","乒乓球","排球"]
    return render(request,'homework/sports.html',{"sport_list":sport_list})

def go_reg(request):
    return render(request,'homework/register.html')

# 注册逻辑处理
def reg(request):
    regName = request.POST.get("regName")
    regPwd = request.POST.get("regPwd")
    sex = request.POST.get("sex")
    return render(request,'homework/success.html',
                  {"reg_name":regName,"reg_pwd":regPwd,"reg_sex":sex})
