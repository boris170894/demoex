from django.contrib import admin

from .models import *

admin.site.register(QualModel)
admin.site.register(SpecModel)
""" admin.site.register(CollegeInfoMoodel) """

@admin.register(GraduateInfoModel)
class GraduateInfoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("fio",)}
    list_display=("fio", "spec", "qual","year_of_admission")
    search_fields = ("year_of_admission","fio")
    