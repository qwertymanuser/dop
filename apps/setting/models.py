from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=230, 
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to="logo",
        verbose_name="Логотип сайта"
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Тел.ном"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    adsress = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    facebook = models.URLField(
        verbose_name="Facebook"
    )
    instagramm = models.URLField(
        verbose_name="Instagramm"
    )


class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="about_image/",
        verbose_name="Фотогрaфия"
    )


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройка сайта"
