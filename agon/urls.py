"""agon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings
from accounts.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('home/', Home.as_view(), name='home'),

    path('administrator/dashboard/',AdminDashboard.as_view(), name='admin_dashboard'),
    path('administrator/admin/list/',AdminList.as_view(), name='admin_list'),
    path('administrator/organizer/list/',OrganizerList.as_view(), name='organizer_list'),
    path('administrator/student/list/',StudentList.as_view(), name='student_list'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

