from django.contrib import admin
from django.urls import path, include
from website import views

admin.site.siteheader = ""
admin.site.site_title = ""
admin.site.index_title = ""

urlpatterns = [
    path("", views.home, name="portfolio"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("projects", views.Projects, name="Projects Page"),

]
