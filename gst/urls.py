"""gst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from auto.views import index,gst_search
from products.views import product_upload
from vendor.views import vendor_profile,update_gst

urlpatterns = [
    path('product-upload', product_upload,name='product_upload'),
    path('vendor-profile', vendor_profile, name='vendor_profile'),
    path('admin/', admin.site.urls),
    path('filter_gst/<str:query>',gst_search , name='filter_first_option'),
    path('update-profile-gst',update_gst , name='update_profile_gst'),
    path('', index, name='index'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
