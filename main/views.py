from django.shortcuts import render
from main.models import *
from about.models import Tools, Stuff, Advantages, HowWeDo, Replies, Partners
from projects.models import Projects, ProjectType
from prices.models import *
from menu.models import MenuBullet
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


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


def main(request):
    main_slides = SliderMain.objects.all()
    block3_items = Block3Main.objects.all()
    sales = Sales.objects.all()
    advantages = Advantages.objects.all()
    howwedo = HowWeDo.objects.order_by('num')
    stuff = Stuff.objects.all()
    tools = Tools.objects.all()
    questions = Questions.objects.all()
    types = ProjectType.objects.all()
    projects_block = Projects.objects.all().filter(main_page=True)
    projects_filter = ''
    try:
        projects_filter = Projects.objects.all().filter(type=types[0])[:4]
    except:
        pass
    data_all = 0

    rem_type = PricesFork.objects.all()[:3]
    place_types = PlaceType.objects.all()
    works = Services.objects.all()

    all_services={}
    for t in rem_type:
        try:
            all_services[t.name] = Services.objects.all().filter(remonttype=t.id)
        except:
            pass

    cats = ServicesCategories.objects.all()
    contacts = Contacts.objects.first()
    menu = MenuBullet.objects.all()
    title = 'Ремонт квартир в Казани под ключ: цены от 1490 руб/м2 | РИАЛстрой Казань'
    description = 'Ремонт квартир в Казани под ключ от 1490 руб. за м2. Ремонт квартир с большой гарантией 3 года. Выезд замерщика и составление сметы бесплатно. ☎ 8 (800) 511-43-26 '
    return render(request, 'index.html', locals())


def thankpage(request):
    sales = Sales.objects.all()
    questions = Questions.objects.all()
    types = ProjectType.objects.all()

    cats = ServicesCategories.objects.all()
    contacts = Contacts.objects.first()
    menu = MenuBullet.objects.all()
    title = 'Спасибо за оставленную заявку'

    return render(request, 'thankpage.html', locals())

def vidyrabot(request):
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


    title = "Виды отделочных и ремонтных работ | РИАЛстрой в Казани"
    description = ""
    return render(request, 'vidyrabot.html', locals())

def politica(request):
    sales = Sales.objects.all()
    questions = Questions.objects.all()
    cats = ServicesCategories.objects.all()
    contacts = Contacts.objects.first()
    menu = MenuBullet.objects.all()
    title = ' Политика конфиденциальности'

    return render(request, 'politica.html', locals())


def service(request, category, subcategory, service):
    contacts = Contacts.objects.first()
    title = Services.objects.get(slug=service).title
    cases = Projects.objects.all()[:3]
    content = Services.objects.get(slug=service).content
    sales = Sales.objects.all()
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    place_types = PlaceType.objects.all()
    works = Services.objects.all()

    all_services={}
    for t in rem_type:
        try:
            all_services[t.name] = Services.objects.all().filter(remonttype=t.id)
        except:
            pass

    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    description = Services.objects.get(slug=service).description

    return render(request, 'detail-page.html', locals())

"""
def type(request, type):
    contacts = Contacts.objects.first()
    title = ProjectType.objects.get(slug=type).name
    cases = ProjectType.objects.get(slug=type).projects_set.all()[:3]
    content = ProjectType.objects.get(slug=type).detail_page_content

    sales = Sales.objects.all()
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    works = Services.objects.all()
    place_types = PlaceType.objects.all()
    cats = ServicesCategories.objects.all()

    all_services={}
    for t in rem_type:
        try:
            all_services[t.name] = Services.objects.all().filter(remonttype=t.id)
        except:
            pass

    menu = MenuBullet.objects.all()

    description = ProjectType.objects.get(slug=type).description

    return render(request, 'detail-page.html', locals())
"""

def project(request, project):
    try:
        t = Projects.objects.get(slug=project).type
        #cases = Projects.objects.filter(type=t)[:3]
        content = Projects.objects.get(slug=project).detail_page_content
        description = Projects.objects.get(slug=project).description
        title = Projects.objects.get(slug=project).title
    except Projects.DoesNotExist:
        pass

    sales = Sales.objects.all()
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    works = Services.objects.all()
    place_types = PlaceType.objects.all()
    contacts = Contacts.objects.first()
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    all_services={}
    for typ in rem_type:
        try:
            all_services[typ.name] = Services.objects.all().filter(remonttype=typ.id)
        except:
            pass

    project = Projects.objects.get(slug=project)
    return render(request, 'detail-page.html', locals())

 
def calculate(request):
    contacts = Contacts.objects.first()
    title = 'Прайс-лист на ремонт квартир, цены на отделочные работы 2018 | РИАЛстрой Казань'
    description = 'Прайс-лист на ремонт квартир 2018. Цены на отделочные и ремонтные работы указаны для того, чтобы вы могли, примерно, рассчитать стоимость вашего ремонта. ☎ 8 (800) 511-43-26 '
    calc = Services.objects.all()
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'pricestable.html', locals())


def all_projects(request):
    contacts = Contacts.objects.first()
    title = 'Фото работ квартир, помещений, офисов, ресторанов| РИАЛстрой Казань'
    types = ProjectType.objects.all()
    projects_filter = Projects.objects.all().filter(type=types[0])
    data_all = 1
    all = True
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'all_projects.html', locals())


def replies(request):
    contacts = Contacts.objects.first()
    title = 'Отзывы о компании РИАЛстрой в Казани'
    replies = Replies.objects.all()
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'replies.html', locals())


def reply(request, reply):
    contacts = Contacts.objects.first()
    title = 'Отзыв'
    project = Projects.objects.get(slug=reply)
    a = True
    cats = ServicesCategories.objects.all()

    menu = MenuBullet.objects.all()

    return render(request, 'detail-reply.html', locals())


def fork(request, price):
    sales = Sales.objects.all()
    title = PricesFork.objects.get(slug=price).title
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    works = Services.objects.all()
    place_types = PlaceType.objects.all()
    contacts = Contacts.objects.first()
    cases = Projects.objects.all()[:3]
    cats = ServicesCategories.objects.all()

    all_services={}
    for t in rem_type:
        try:
            all_services[t.name] = Services.objects.all().filter(remonttype=t.id)
        except:
            pass


    content = PricesFork.objects.get(slug=price).content
    menu = MenuBullet.objects.all()
    description = PricesFork.objects.get(slug=price).description
    all = PricesFork.objects.get(slug=price)

    return render(request, 'article.html', locals())


def pricelist(request):
    rem_type = PricesFork.objects.all()
    categories = ServicesCategories.objects.all()
    subcategories = ServicesSubcategories.objects.all()
    works = Services.objects.all()
    cats = ServicesCategories.objects.all()

    all_services={}
    for t in rem_type:
        try:
            all_services[t.name] = Services.objects.all().filter(remonttype=t.id)
        except:
            pass


    contacts = Contacts.objects.first()

    title = 'Стоимость  ремонта квартиры в Казани: цены на ремонт 2018'
    description = 'Предлагаем ремонт квартиры по цене от 1490 руб. за м2 в 2018 году. Давайте рассчитаем стоимость ремонта вашей квартиры?  ☎ 8 (800) 511-43-26 '

    menu = MenuBullet.objects.all()

    return render(request, 'pricelist.html', locals())

"""
def subcategory(request, category, subcategory):
    sales = Sales.objects.all()
    title = ServicesSubcategories.objects.get(slug=subcategory).name
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    works = Services.objects.all()
    place_types = PlaceType.objects.all()
    contacts = Contacts.objects.first()
    cases = Projects.objects.all()[:3]
    cats = ServicesCategories.objects.all()

    all_services={}
    for t in rem_type:
        try:
            all_services[t.name] = Services.objects.all().filter(remonttype=t.id)
        except:
            pass


    content = ServicesSubcategories.objects.get(slug=subcategory).content

    menu = MenuBullet.objects.all()

    description = ServicesSubcategories.objects.get(slug=subcategory).description

    return render(request, 'detail-page.html', locals())


def category(request, category):
    sales = Sales.objects.all()
    title = ServicesCategories.objects.get(slug=category).name
    types = ProjectType.objects.all()
    rem_type = PricesFork.objects.all()[:3]
    works = Services.objects.all()
    place_types = PlaceType.objects.all()
    contacts = Contacts.objects.first()
    cases = Projects.objects.all()[:3]
    cats = ServicesCategories.objects.all()
        
    all_services={}
    for t in rem_type:
        try:
            all_services[t.name] = Services.objects.all().filter(remonttype=t.id)
        except:
            pass


    content = ServicesCategories.objects.get(slug=category).content

    menu = MenuBullet.objects.all()

    description = ServicesCategories.objects.get(slug=category).description

    return render(request, 'detail-page.html', locals())
"""
def errorhandler(request):
    sales = Sales.objects.all()
    questions = Questions.objects.all()
    types = ProjectType.objects.all()

    cats = ServicesCategories.objects.all()
    contacts = Contacts.objects.first()
    menu = MenuBullet.objects.all()
    title = 'Ошибка, страница не найдена'

    return render_to_response('error.html', locals())

def sitemap(request):
    sales = Sales.objects.all()
    questions = Questions.objects.all()
    types = ProjectType.objects.all()

    cats = ServicesCategories.objects.all()
    contacts = Contacts.objects.first()
    menu = MenuBullet.objects.all()
    #title = 'Ошибка, страница не найдена'

    return render_to_response('sitemap.html', locals())
    
@csrf_exempt
def send_mail(request):
    r = request.POST

    if len(r) != 0:
        name = r.get('name')
        phone = r.get('phone')
        type = r.get('type')
        msg = '{}\nИмя: {}\nТелефон: {}'.format(type, name, phone)
        if type == "Заявка на ремонт":
            place_type = r.get('place-type')
            repair_type = r.get('repair-type')
            square = r.get('square')
            design = r.get('design')
            works = r.get('works')
            msg = msg + '\nТип помещения: {}\nТип ремонта: {}\nПлощадь: {}\nДизайн проект: {}\nВиды работ: {}'.format(place_type,
                                                                                                         repair_type,
                                                                                                         square,
                                                                                                         design,
                                                                                                         works)

        email = EmailMessage(type, msg, to=['tdk1243@mail.ru','Sheahmetovr@mail.ru','prosozdanie@yandex.ru'])
        email.send()

    return JsonResponse(r)