"""stin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from  django.conf import settings
from django.conf.urls.static import static
from main import models,views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home/$',views.home,name='home'),
    url(r'^aboutus/$',views.aboutus,name='aboutus'),
    url(r'^userPage/$',views.userPage,name='userPage'),
    url(r'^userProfile/$',views.UserProfil,name='userProfile'),
    url(r'^userAddProducte/$',views.userAddProducte,name='userAddProducte'),
    url(r'^userUpdate/$',views.userUpdate,name='userUpdate'),
    url(r'^showCart/$',views.showCart,name='showCart'),
    url(r'^deleteProdcutCart/(?P<pk>\d+)/$', views.deleteProdcutCart, name='deleteProdcutCart'),
    url(r'^userChangePassword/$',views.userChangePassword,name='userChangePassword'),
    url(r'^panel/listproducte/$',views.listProducte,name='listproducte'),
    url(r'^home/producte/(?P<pk>\d+)/$', views.producte, name='producte'),
    url(r'^order/addtocart/(?P<pk>\d+)/$', views.AddToCart, name='AddToCart'),
    url(r'^home/producte/addComment/(?P<pk>\d+)/$', views.addComment, name='addComment'),
    url(r'^home/producteCategory/(?P<pk>\d+)/$', views.producteCategory, name='producteCategory'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^panel/deleteMessage/(?P<pk>\d+)/$', views.deleteMessage, name='deleteMessage'),
    url(r'^panel/ediTP/(?P<pk>\d+)/$', views.ediTP, name='ediTP'),
    url(r'^panel/deteteP/(?P<pk>\d+)/$', views.deteteP, name='deteteP'),
    url(r'^panel/$',views.panel,name='panel'),
    url(r'^panel/setting',views.setting,name='setting'),
    url(r'^contantus',views.contantus,name='contantus'),
    url(r'^panel/addCategory/$',views.addCategory,name='addCategory'),
    url(r'^panel/listMessage/',views.listMessage,name='listMessage'),
    url(r'^panel/listCategory/$',views.listCategory,name='listCategory'),
    url(r'^panel/addProducte/$', views.addProducte, name='addProducte'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
