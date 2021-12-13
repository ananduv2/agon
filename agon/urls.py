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
    path('signup/',StudentSignUP.as_view(), name='signup'),

    path('administrator/dashboard/',AdminDashboard.as_view(), name='admin_dashboard'),
    path('administrator/admin/list/',AdminList.as_view(), name='admin_list'),
    path('administrator/student/list/',StudentList.as_view(), name='student_list'),
    path('administrator/add/event/',AddEvent.as_view(), name='add_event'),
    path('administrator/edit/event/<id>/',EditEvent.as_view(), name='edit_event'),
    path('administrator/delete/event/<id>/',DeleteEvent.as_view(), name='delete_event'),
    path('administrator/entry/view/<id>/',ViewEntries.as_view(), name='view_entry'),
    path('administrator/pubish/result/<id>/',PublishResult.as_view(), name='publish_result'),
    path('administrator/approve/entry/<id>/',ApproveEntry.as_view(), name='approve_entry'),
    path('administrator/reject/entry/<id>/',RejectEntry.as_view(), name='reject_entry'),
    path('administrator/add/liveevent/',AddLiveEvent.as_view(), name='add_live_event'),
    path('administrator/edit/profile/',EditAdminProfile.as_view(), name='edit_admin_profile'),

    path('student/dashboard/',StudentDashboard.as_view(), name='student_dashboard'),
    path('student/submit/entry/<id>/',SubmitEntry.as_view(), name='submit_entry'),
    path('student/edit/profile/',EditProfile.as_view(), name='edit_student_profile'),

    path('user/events/',ViewEvents.as_view(), name='view_events'),
    path('user/live/events/',ViewLiveEvents.as_view(), name='view_liveevents'),
    path('user/results/',ViewResults.as_view(), name='view_results'),
    path('user/view/entries/<id>/',PublicEntryView.as_view(), name='view_public_entries'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

