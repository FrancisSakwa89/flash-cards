from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.core.urlresolvers import reverse
from . import views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/card$',views.newcard, name='newcard'),
    url(r'^profile/(\d+)', views.profile, name='profile'), 
    url(r'^new/profile$',views.newprofile, name='newprofile'),
    url(r'^new/card$',views.newcard, name='newcard'),
    url(r'^card/', views.card, name='card'),

]    

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
