from django.conf import settings
from django.conf.urls import url, include

from voting.website import admin
from voting.website import views

slug = r'[a-z0-9-]+'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns += [
    url(r'^accounts/', include('voting.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
