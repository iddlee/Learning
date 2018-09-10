from django.shortcuts import render
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def go_upload(request):
    return render(request,'myupload.html')

def upload(request):
    upload_obj = request.FILES.get("myfile")   # 接收域名为"myfile"的上传文件
    dest_file = os.path.join(BASE_DIR,'upload','uploadimg',upload_obj.name) # 拼接上传文件的目标文件
    with open(dest_file,'wb') as f:   # 以"wb"模式打开上传目标文件，准备写入
        for chunk in upload_obj.chunks():   # 对上传文件进行分块写入
            f.write(chunk)

    imgpath = 'uploadimg/'+upload_obj.name   # 取得刚才上传文件的网址
    return render(request,'success.html',{'imgpath':imgpath})

