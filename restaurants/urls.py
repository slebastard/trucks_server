from django.conf.urls import url

from . import views_test
from . import views_restaurants
from . import views_command

urlpatterns = [
    url(r'^test.json$', views_test.show_test),
    url(r'^restaurants.json$', views_restaurants.show_resto),
    url(r'^generate_command.json$', views_command.generate_command)
]
