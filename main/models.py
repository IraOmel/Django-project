from django.db import models


# Create your models here.
class App(models.Model):
    name = models.CharField("Назва", max_length=100)
    name_header = models.CharField("Повна назва", max_length=250)
    img_project = models.ImageField(upload_to="images/", verbose_name="Фото проекту")
    name_project = models.CharField("Назва проекту", max_length=50)
    info_about = models.TextField("Інформація про проект")
    order = models.CharField("Замовник", max_length=100)
    adress = models.CharField("Адреса", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекти"


class User(models.Model):
    Name = models.CharField("Користувач", max_length=150)
    Email = models.EmailField("Поштова адреса")
    Message = models.CharField("Повідомлення", max_length=300)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"


class Projects(models.Model):
    name = models.CharField("Назва", max_length=100)
    eng_name = models.CharField("Name", max_length=100, default='#')
    short_info = models.CharField("Короткий опис", max_length=50, blank=True)
    img_project = models.ImageField(upload_to="images/", verbose_name="Фото проекту")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Коротка інформація"
        verbose_name_plural = "Список всіх проектів"

