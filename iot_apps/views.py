from django.shortcuts import render,HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is service page")

def contact(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    desc = request.POST.get("desc")
    # contact = contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
    # contact.save()


    return render(request, 'contact.html')
    # return HttpResponse("this is contacts page")
