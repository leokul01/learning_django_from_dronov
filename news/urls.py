from django.urls import path, re_path
from django.views.generic.dates import ArchiveIndexView
from news.views import NewsArchiveView, YearNewsArchiveView
from news.models import New

urlpatterns = [
    path('', NewsArchiveView.as_view(), name = 'news_archive'),
    re_path(r'^(?P<year>\d{4})/$', YearNewsArchiveView.as_view(), name = 'year_archive'),
    # path('', ArchiveIndexView.as_view(model = New, date_field = 'pub_date', template_name = 'news/index.html'), name = 'news_archive'),
]