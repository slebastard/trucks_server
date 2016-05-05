from django.conf.urls import url

from . import views_test

urlpatterns = [
    url(r'^test.json$', views_test.show_test)
]
