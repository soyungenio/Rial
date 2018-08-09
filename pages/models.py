from django.db import models
from tinymce.models import HTMLField


class Pages(models.Model):
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
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'