from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic
from.forms import InqiryForm
from django.views.generic.base import TemplateView

# Create your views here.
def index(request):
    return render(request,'diary/index.html')

class IndexView(generic.TemplateView):
    template_name="diary/index.html"

class Inquiryview(generic.FormView):
    template_name ="diary/inquiry.html"
    form_class =InqiryForm