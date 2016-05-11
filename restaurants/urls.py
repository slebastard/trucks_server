from django.conf.urls import url

from . import views_test
from . import views_restaurants

urlpatterns = [
    url(r'^test.json$', views_test.show_test),
    url(r'^restaurants.json$', views_restaurants.show_resto)
]
