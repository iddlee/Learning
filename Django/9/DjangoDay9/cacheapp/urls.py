from django.urls import path
from cacheapp.views import *

urlpatterns = [
    path('cake/<cake_id>/',get_cake),
    path('cakes/',my_view),
    path('all/',my_view),
    path('allcakes/',cache_page(30)(cakes_views)),
]