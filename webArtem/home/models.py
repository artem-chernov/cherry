from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(verbose_name=u"Как Вас зовут?", max_length=34)
    telephone = models.PositiveIntegerField(verbose_name=u"Телефон", max_length=34)
    email = models.EmailField(verbose_name=u"Почта", max_length=34)
