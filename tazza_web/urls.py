"""
URL configuration for tazza_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from tazza_web import views
from django.conf import settings
from django.conf.urls.static import static 

# user = admin
# pass = admin123

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('gallery/', views.gallery,name='gallery'),
    path('product/<int:myid>/', views.product, name='product'),
    path('error/', views.error,name='error'),
    path('all_product/', views.all_product,name='all_product'),
    
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)