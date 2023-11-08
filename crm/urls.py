"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from website.views import (
    delete_record,
    home,
    # login_user,
    logout_user,
    register_user,
    customer_record,
    delete_record,
    add_record,
    update_record
)

urlpatterns = [
    path("", home, name="home"),
    # path('login/', login_user, name='login'),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
    path("record/<int:pk>", customer_record, name="record"),
    path("delete_record/<int:pk>", delete_record, name="delete_record"),
    path("add_record/", add_record, name="add_record"),
    path("update_record/<int:pk>", update_record, name="update_record"),
    path("admin/", admin.site.urls),
]
