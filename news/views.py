from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from news.models import New
from goods.models import Category

class NewsArchiveView(ArchiveIndexView):
    model = New
    date_field = 'pub_date'
    template_name = 'news/index.html'

    def get_context_data(self, **kwargs):
        context = super(NewsArchiveView, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.order_by('name')
        return context

class YearNewsArchiveView(YearArchiveView):
    model = New
    date_field = 'pub_date'
    template_name = 'news/year_archive.html'
    make_object_list = True

    def get_context_data(self, **kwargs):
        context = super(YearNewsArchiveView, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.order_by('name')
        return context
