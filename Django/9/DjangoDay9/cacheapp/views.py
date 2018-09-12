from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from cacheapp.models import Cake

def get_cake(request,cake_id):
    value = cache.get("cake_"+cake_id)  # 使用底层cache API尝试获取缓存中的数据
    if value:   # 缓存中存在
        return render(request,'cake.html',{"cake":value,"msg":"恭喜，缓存命中了!"})
    else:   # 缓存中不存在
        cake = Cake.objects.get(id=cake_id)    # 查询MySQL数据库
        cache.set("cake_"+cake_id,cake,30)      # 设置缓存
        return render(request,'cake.html',{"cake":cake,"msg":"从MySQL数据库中查询的数据..."})


count = 0

@cache_page(30)  # 缓存视图结果30秒
def my_view(request):
    global count
    count += 1
    print("第"+str(count)+"次调用my_view()视图函数")
    cakes = Cake.objects.all()  # 查询MySQL数据库
    return render(request, 'cakes.html', {"cakes": cakes, "msg": "第"+str(count)+"次调用my_view()视图函数"})



def cakes_views(request):
    print("调用cakes_views()视图函数")
    cakes = Cake.objects.all()  # 查询MySQL数据库
    return render(request, 'cakes.html', {"cakes": cakes})
