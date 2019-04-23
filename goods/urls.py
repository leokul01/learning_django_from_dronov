from django.urls import path, re_path
# from . import views
from goods.twviews import GoodListView, GoodDetailView

urlpatterns = [
    # re_path(r'^(?:(?P<cat_id>\d+)/)?$', views.index, name = 'index'),
    re_path(r'^(?:(?P<cat_id>\d+)/)?$', GoodListView.as_view(), name = 'index'),
    # path('good/<int:good_id>', views.good, name = 'good')
    path('good/<int:good_id>', GoodDetailView.as_view(), name = 'good'),
]