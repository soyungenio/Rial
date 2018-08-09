from django.shortcuts import render
from main.models import *
#from about.models import Tools, Stuff, Advantages, HowWeDo, Replies
from projects.models import Projects, ProjectType
from prices.models import *
from menu.models import *
from pages.models import *

def page(request, category):
    contacts = Contacts.objects.first()
    cases = Projects.objects.all()[:3]
    sales = Sales.objects.all()
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    place_types = PlaceType.objects.all()
    works = Services.objects.all()
    cats = ServicesCategories.objects.all()
    menu = MenuBullet.objects.all()

    all_services={}
    for t in rem_type:
        try:
            all_services[t.name] = Services.objects.all().filter(remonttype=t.id)
        except:
            pass

    try:
        all = Page.objects.get(slug=category)
        title = Page.objects.get(slug=category).title
        content = Page.objects.get(slug=category).content
        description = Page.objects.get(slug=category).description
        return render(request, 'article.html', locals())
    except:
        pass
    try:
        all = ServicesCategories.objects.get(slug=category)
        title = ServicesCategories.objects.get(slug=category).title
        content = ServicesCategories.objects.get(slug=category).content
        description = ServicesCategories.objects.get(slug=category).description
        return render(request, 'article.html', locals())
    except:
        pass
    
    try:
        all = ProjectType.objects.get(slug=category)
        title = ProjectType.objects.get(slug=category).title
        cases = ProjectType.objects.get(slug=category).projects_set.all()[:3]
        content = ProjectType.objects.get(slug=category).detail_page_content
        description = ProjectType.objects.get(slug=category).description
        return render(request, 'article.html', locals())
    except:
        pass

    try:
        all = MenuBullet.objects.get(slug=category)
        title = MenuBullet.objects.get(slug=category).title
        content = MenuBullet.objects.get(slug=category).content
        description = MenuBullet.objects.get(slug=category).description
        return render(request, 'article.html', locals())
    except:
        pass

    try:
        all = Pages.objects.get(slug=category)
        title = Pages.objects.get(slug=category).title
        content = Pages.objects.get(slug=category).content
        description = Pages.objects.get(slug=category).description
        return render(request, 'article.html', locals())
    except:
        pass
        
    return render(request, 'error.html', locals())

def page2(request, category, subcategory):
    contacts = Contacts.objects.first()
    cases = Projects.objects.all()[:3]
    sales = Sales.objects.all()
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    place_types = PlaceType.objects.all()
    works = Services.objects.all()
    cats = ServicesCategories.objects.all()
    menu = MenuBullet.objects.all()

    all_services={}
    for t in rem_type:
        try:
            all_services[t.name] = Services.objects.all().filter(remonttype=t.id)
        except:
            pass

    try:
        all = Page2.objects.get(slug=subcategory)
        title = Page2.objects.get(slug=subcategory).title
        content = Page2.objects.get(slug=subcategory).content
        description = Page2.objects.get(slug=subcategory).description
        return render(request, 'article.html', locals())
    except:
        pass
    try:
        all = ServicesSubcategories.objects.get(slug=subcategory)
        title = ServicesSubcategories.objects.get(slug=subcategory).title
        content = ServicesSubcategories.objects.get(slug=subcategory).content
        description = ServicesSubcategories.objects.get(slug=subcategory).description
        return render(request, 'article.html', locals())
    except:
        pass
        
    return render(request, 'error.html', locals())
