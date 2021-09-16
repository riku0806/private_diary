from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
import re
from django.core.mail import message
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse
from django.shortcuts import render
import logging
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView
from .forms import DiaryCreateForm, InquiryForm

# Create your views here.
logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "diary/index.heml"


class InquiryVie(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')


def index(request):
    return render(request, 'diary/index.html')


class IndexView(generic.TemplateView):
    template_name = "diary/index.html"


class InquiryView(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('Inquiry sent by{}'.format(form.cleaned_data['name']))
        message.success(self.request, 'メッセージ')
        return super().form_valid(form)


class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'

    def get_queryset(self):
        diaries = Diary.objects.filter(
            user=self.request.user).order_by('-created_at')
        return diaries


class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary/diary_detail.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        message.success(self.request, '日記')
        return super().form_valid(form)

        def form_invalid(self, form):
            message.error(self.request, "日記の作成")
            return super().form_invalid(form)


class DiaryUpdateView(LoginRequiredMixin, generic, UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    form_class = DiaryCreateForm

    def get_success_url(self):
        return reverse_lazy('diary:diary_detail', kwargs={'pk': self.kwargs['pk']})
    def form_valid(self, form):
        message.success(self.request, '日記')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "失敗")
        return super().form_invalid(form)


class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary_list')

    def delete(self, request, *args, **kwargs):
        message.success(self.request, "日記")
        return super().delete(request, *args, **kwargs)
