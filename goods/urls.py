from django.urls import path, re_path
from goods.views import GoodListView, GoodDetailView

urlpatterns = [
    re_path(r'^(?:(?P<cat_id>\d+)/)?$', GoodListView.as_view(), name = 'index'),
    path('good/<int:good_id>', GoodDetailView.as_view(), name = 'good'),
]