from django.db import models
from tinymce.models import HTMLField


class MenuBullet(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Заголовок")
    name = models.CharField(max_length=256, blank=True, null=True, default=None, 
                            verbose_name=u"Название")
                    
    slug = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"URL страницы")

    content = HTMLField(blank=True, null=True, default=None,
                            verbose_name=u"Контент на детальной странице")
    description = models.CharField(max_length=256, blank=True, null=True, default=None)
    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class Page(models.Model):
    menu = models.ForeignKey(MenuBullet, blank=True, null=True, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Заголовок")
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Название")
    slug = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"URL страницы")
    content = HTMLField(default=None, verbose_name=u"Контент на детальной странице")
    description = models.CharField(max_length=256, blank=True, null=True, default=None)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Страница 1 уровня'
        verbose_name_plural = 'Страницы 1 уровня'


class Page2(models.Model):
    page = models.ForeignKey(Page, blank=True, null=True, default=None, on_delete=models.CASCADE,
                             verbose_name=u"Страница родительская")
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Заголовок")
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Название")
    slug = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"URL страницы")
    content = HTMLField(default=None, verbose_name=u"Контент на детальной странице")
    description = models.CharField(max_length=256, blank=True, null=True, default=None)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Страница 2 уровня'
        verbose_name_plural = 'Страницы 2 уровня'

