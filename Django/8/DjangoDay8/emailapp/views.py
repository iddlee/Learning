from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from emailapp.models import Email


def go_email(request):
    return render(request,'email.html')

def get_emails(request,state_code):
    emails_queryset = Email.objects.filter(state=state_code)  # 根据传递的状态参数，获取相应的邮件
    email_list = []
    for email in emails_queryset:
        email_dict = {}
        email_dict["id"] = email.id
        email_dict["title"] = email.title
        email_dict["content"] = email.content
        email_dict["sender"] = email.sender
        email_list.append(email_dict)
    return JsonResponse({"emails":email_list})





