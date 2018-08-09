from django.shortcuts import render
from about.models import *
from main.models import Contacts
from prices.models import ServicesCategories
from menu.models import MenuBullet

# Create your views here.
def about(request):
    advantages = Advantages.objects.all()
    howwedo = HowWeDo.objects.order_by('num')
    stuff = Stuff.objects.all()
    tools = Tools.objects.all()
    partners = Partners.objects.all()
    replies = Replies.objects.all()[:3]
    contacts = Contacts.objects.first()
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    title = 'О компании'
    return render(request, 'about.html', locals())


def advantages(request):
    advantages = Advantages.objects.all()
    contacts = Contacts.objects.first()
    title = 'Преимущества'
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()
    return render(request, 'advantages.html', locals())


def contacts(request):
    contacts = Contacts.objects.first()
    title = 'Контакты'
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()
    return render(request, 'contacts.html', locals())