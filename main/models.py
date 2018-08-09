from django.db import models
from tinymce.models import HTMLField
from about.models import Stuff


class SliderMain(models.Model):
    title_img = models.ImageField(upload_to='static/img', blank=True, null=True, default=None,
                                  verbose_name=u"Иконка в заголовке")
    title = HTMLField(default=None, verbose_name=u"Заголовок")
    text = HTMLField(default=None, verbose_name=u"Текст")
    button_text = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Текст на кнопке")
    href = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Ссылка (если попап - оставить поле пустым)")
    background = models.ImageField(upload_to='static/img/main', verbose_name=u"Фоновая картинка")

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Слайд первого экрана'
        verbose_name_plural = 'Слайды первого экрана'


class Block3Main(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Заголовок")
    img = models.ImageField(upload_to='static/img/block3', blank=True, null=True, default=None,
                                  verbose_name=u"Фоновая картинка")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Блок 3 - ремонт квартир'


class Block3MainText(models.Model):
    block = models.ForeignKey(Block3Main, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text = HTMLField(default=None, verbose_name=u"Пункт элемента")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Пункт элемента'
        verbose_name_plural = 'Пункты элемента'


class Sales(models.Model):
    title1 = HTMLField(default=None, verbose_name=u"Заголовок 1")
    title2 = HTMLField(default=None, verbose_name=u"Заголовок 2")
    text = HTMLField(default=None, verbose_name=u"Текст")
    img = models.ImageField(upload_to='static/img/block9', blank=True, null=True, default=None,
                                  verbose_name=u"Фоновая картинка")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции и скидки'


class Questions(models.Model):
    person = models.ForeignKey(Stuff, blank=True, null=True, default=None, on_delete=models.CASCADE)
    question = HTMLField(default=None, verbose_name=u"Вопрос")
    answer = HTMLField(default=None, verbose_name=u"Ответ")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Вопрос - Ответ'
        verbose_name_plural = 'Вопрос - Ответ'


class Contacts(models.Model):
    address = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Адрес")
    time = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Время работы")
    email = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"E-mail")
    map = models.TextField(blank=True, null=True, default=None, verbose_name=u"Код карты (ширину и высоту на 100%)")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class ContactsPhones(models.Model):
    contact = models.ForeignKey(Contacts, blank=True, null=True, default=None, on_delete=models.CASCADE)
    phone = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Телефон")

    def __str__(self):
        return '%s' % self.phone

    class Meta:
        verbose_name = 'Телефоны'
        verbose_name_plural = 'Номера телефонов'


class ContactsBusiness(models.Model):
    contact = models.ForeignKey(Contacts, blank=True, null=True, default=None, on_delete=models.CASCADE)
    business = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Реквизиты (инн, кпп и т.д.)")

    def __str__(self):
        return '%s' % self.business

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'


class Socials(models.Model):
    contact = models.ForeignKey(Contacts, blank=True, null=True, default=None, on_delete=models.CASCADE)
    href = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Ссылка")
    img = models.ImageField(upload_to='static/img/', blank=True, null=True, default=None,
                                  verbose_name=u"Иконка")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Соц сеть'
        verbose_name_plural = 'Соц сети'
