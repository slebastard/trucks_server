from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'trucks_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^restaurants/', include('restaurants.urls')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('^', include('django.contrib.auth.urls'))
]
