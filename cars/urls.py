from django.conf.urls import include,url
from .views import ModelCreate,PartsCreate,homepage,ViewTable ,GraphView

urlpatterns=[
    url(r'model_create/$',
        ModelCreate.as_view(),
        name = 'car_model_create'),

    url(r'parts_create/$',
        PartsCreate.as_view(),
        name = 'car_parts_create'),


    url(r'^$',
        homepage,
        name='homepage_list'),

    url(r'table/$',
        ViewTable,
        name='table_view'),
    url(r'graph/$',
        GraphView,
        name='graph_view'),
]
