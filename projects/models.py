from django.db import models
from tinymce.models import HTMLField
from about.models import Replies


class ProjectType(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                        verbose_name=u"Заголовок")
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Название")
    price = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Цена")
    terms = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Сроки")
    img = models.ImageField(upload_to='static/img/block1', blank=True, null=True, default=None,
                                  verbose_name=u"Фоновая картинка")
    detail_page_content = HTMLField(default=None, verbose_name=u"Контент детальной страницы")
    slug = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"URL страницы")
    description = models.CharField(max_length=256, blank=True, null=True, default=None)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Тип помещения'
        verbose_name_plural = 'Типы помещений'


class Projects(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Заголовок")
    name = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u"Название")
    price = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u'Цена')
    time = models.CharField(max_length=256, blank=True, null=True, default=None, verbose_name=u'Срок (дней)')
    square = models.IntegerField(default=0, verbose_name=u'Площадь (м2)')
    type = models.ForeignKey(ProjectType, blank=True, null=True, default=None, on_delete=models.CASCADE)
    reply = models.ForeignKey(Replies, blank=True, null=True, default=None, on_delete=models.CASCADE)
    design = models.BooleanField(default=False, verbose_name=u"Дизайн проект")
    detail_page_content = HTMLField(default=None, verbose_name=u"Контент детальной страницы")
    works = HTMLField(blank=True, null=True, default=None, verbose_name=u"Выполненные работы")
    main_page = models.BooleanField(default=False, verbose_name=u"На главную")
    slug = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"URL страницы")
    description = models.CharField(max_length=256, blank=True, null=True, default=None)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectImages(models.Model):
    project = models.ForeignKey(Projects, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/img/cases', blank=True, null=True, default=None,
                            verbose_name=u"Фото")
    is_main = models.BooleanField(default=False, verbose_name=u"Главное фото")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фото проекта'
        verbose_name_plural = 'Фото проектов'
        ordering = ["-is_main"]


