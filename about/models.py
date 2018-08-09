from django.db import models
from tinymce.models import HTMLField



class Advantages(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Заголовок")
    text = HTMLField(default=None, verbose_name=u"Подзаголовок")
    icon = models.ImageField(upload_to='static/img/block2/', blank=True, null=True, default=None,
                                  verbose_name=u"Иконка")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class AdvantagesBullets(models.Model):
    block = models.ForeignKey(Advantages, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text = HTMLField(default=None, verbose_name=u"Пункт")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'


class HowWeDo(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Заголовок")
    text = HTMLField(default=None, verbose_name=u"Текст")
    num = models.IntegerField(default=0, verbose_name=u'Порядковый номер')

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Как мы работаем'


class Stuff(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Имя")
    job = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Должность")
    img = models.ImageField(upload_to='static/img/block11/', blank=True, null=True, default=None,
                                  verbose_name=u"Фото")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Персонал'


class StuffBullets(models.Model):
    stuff = models.ForeignKey(Stuff, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text = HTMLField(default=None, verbose_name=u"Пункт")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'


class Tools(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Название")
    img = models.ImageField(upload_to='static/img/block12/', blank=True, null=True, default=None,
                                  verbose_name=u"Фото")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class ToolsBullets(models.Model):
    stuff = models.ForeignKey(Tools, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text = HTMLField(default=None, verbose_name=u"Пункт")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'


class Replies(models.Model):
    img = models.ImageField(upload_to='static/img/replies/', blank=True, null=True, default=None,
                                  verbose_name=u"Фото")
    name = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Имя")
    age = models.IntegerField(blank=True, null=True, default=None, verbose_name=u"Возраст")
    address = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Адрес")
    text = HTMLField(default=None, verbose_name=u"Отзыв")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


from projects.models import Projects


class Partners(models.Model):
    img = models.ImageField(upload_to='static/img/partners/', blank=True, null=True, default=None,
                                  verbose_name=u"Лого")
    name = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Название")
    project = models.ForeignKey(Projects, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'