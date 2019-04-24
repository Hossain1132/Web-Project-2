
from django.conf.urls import include,url
from django.contrib import admin
from . import views



urlpatterns = [
    #url(r'^$', views.index_redirect, name='index_redirect'),
	url(r'^show/', views.show, name='show'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^crud/', include('crud.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/', views.welcome, name='welcome'),
	
    
]
