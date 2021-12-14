from django.urls import path

from .views import index, reset, id_gt_15, has_a_price_bw_150_250, num_lt_50_or_gt_100, delete_chinese, magic

urlpatterns = [
    path('', index, name='index'),

    path('reset/', reset, name='reset'),
    path('id_gt_15', id_gt_15, name='id_gt_15'),
    path('has_a_price_bw_150_250/', has_a_price_bw_150_250, name='has_a_price_bw_150_250'),
    path('num_lt_50_or_gt_100/', num_lt_50_or_gt_100, name='num_lt_50_or_gt_100'),
    path('delete_chinese/', delete_chinese, name='delete_chinese'),

    path('magic/', magic, name='magic'),

]