from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'func_template.html')

class Index2(TemplateView):
    template_name = 'class_template.html'


