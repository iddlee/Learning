from django.shortcuts import render
import memcache
from cacheapp.models import Cake

def memcached_getdata(request,cake_id):
    mc = memcache.Client(["127.0.0.1:11211"])
    value = mc.get("cake_"+cake_id)  # 从Memcahed缓存系统中获取key为"cake"的值
    if value:   # 如果从缓存中查到了，则直接返回
        return render(request,'cake.html',{'msg':'恭喜，缓存命中!','cake':value})
    else:   # 缓存没有找到的情况
        cake = Cake.objects.get(id=cake_id)   # 从MySQL数据库查询
        mc.set("cake_"+cake_id,cake,30)   # 将数据存储到Memcached中，保存30秒
        return render(request, 'cake.html', {'msg': '这是从MySQL中查到的...', 'cake': cake})
