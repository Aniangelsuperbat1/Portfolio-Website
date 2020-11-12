from django.shortcuts import render, HttpResponse
from website.models import Contact
# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        Database = Contact(name=name, email=email, phone=phone, desc=desc)
        Database.save()

    return render(request, "contact.html")


def Projects(request):
    return render(request, "projects.html")
