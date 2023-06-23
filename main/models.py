from django.db import models
from django.urls import reverse

class SpecModel(models.Model):

    spec_name = models.CharField(verbose_name='Специальность', max_length=200)

    def __str__(self):
        return self.spec_name

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class QualModel(models.Model):

    qual_name = models.CharField(verbose_name='Квалификация', max_length=200)

    def __str__(self):
        return self.qual_name

    class Meta:
        verbose_name = 'Квалификация'
        verbose_name_plural = 'Квалификации'


class GraduateInfoModel(models.Model):

    fio = models.CharField(verbose_name='ФИО', max_length=100)
    foto = models.ImageField(verbose_name='Фото', upload_to='uploads/graduates/foto/', blank=True)
    spec = models.ForeignKey('SpecModel', on_delete = models.PROTECT, verbose_name='Специальность')
    qual = models.ForeignKey('QualModel', on_delete = models.PROTECT, verbose_name='Квалификация')
    year_of_admission = models.DateField(verbose_name='Дата поступления')
    year_of_issue = models.DateField(verbose_name='Дата выпуска')
    diplom = models.ImageField(verbose_name='Диплом', upload_to='uploads/graduates/diplom/', blank=True)
    pril_ru = models.ImageField(verbose_name='Приложение РУ', upload_to='uploads/graduates/prilru/', blank=True)
    pril_kaz = models.ImageField(verbose_name='Приложение КАЗ', upload_to='uploads/graduates/prilkaz/', blank=True)
    skill_pass = models.ImageField(verbose_name='Skills-паспорт', upload_to='uploads/graduates/skills_pass/', blank=True)
    ytb_url = models.CharField(verbose_name='Видео', max_length=500, blank=True)
    slug = models.SlugField(unique=True, max_length=100, verbose_name="URL", db_index=True)
    

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return reverse('graduate', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Выпускник'
        verbose_name_plural = 'Выпускники'

class CollegeInfoMoodel(models.Model):

    addr = models.CharField(verbose_name='Адрес', max_length=100)
    tel = models.CharField(verbose_name='Телефон', max_length=25)
    e_mail = models.CharField(verbose_name='e-mail', max_length=20)

    def __str__(self):
        return "Инфо о колледже"

    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'Инфо'