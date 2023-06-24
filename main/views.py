from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic.list import ListView

from .models import GraduateInfoModel, CollegeInfoMoodel


""" 
class graduateInfoView(View):
    def get(self,request,pk):
        graduate_info = GraduateInfoModel.objects.get(id=pk)
        return render(request, 'main/graduate.html', {"graduate_info":graduate_info})

 """

class graduateInfoView(View):
    def get(self,request,slug):
        graduate_info = GraduateInfoModel.objects.get(slug=slug)
        return render(request, 'main/graduate.html', {"graduate_info":graduate_info})


def show_info(request, slug):
    graduate = get_object_or_404(GraduateInfoModel, slug = slug)

    context = {
        "graduate_info" : graduate,
    }

    return render(request, 'main/graduate.html', context=context)

def index(request):
    return render(request, 'main/index.html')

""" def grad_list(request):
    context = GraduateInfoModel.objects.all()
    return render(request, 'main/graduate_list.html', {"context":context}) """

"""     
class collegeInfoView(View):
    def get(self,request):
        college_info = CollegeInfoMoodel.objects.all()
        return render(request, 'main/include/footer.html', {"college_info":college_info}) """