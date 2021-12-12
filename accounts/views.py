from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm
from django.template import RequestContext

import datetime
from django.utils import timezone

from .models import *
from .functions import *
# Create your views here.

class IndexView(View):
    def get(self, request):
        try:
            user = request.user
            context={'user': user}
        except:
            context = {}
        return render(request, 'common/index.html',context)

class LoginView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('home')
            # return HttpResponse("Logged In")
        else:
            msg=""
            return render(request,'common/login.html',{'msg':msg})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # return HttpResponse("Logged In")
        else:
            msg = "Invalid login credentials"
            return render(request,'common/login.html',{'msg':msg})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class Home(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                u = Account.objects.get(user=user)
                if u.type == 'admin':
                    return redirect('admin_dashboard')
                    # return HttpResponse("Admin Dashboard")
                elif u.type == 'organizer':
                    return HttpResponse("Service Provider")
                    # return redirect('provider_dashboard')
                elif u.type == 'student':
                    return HttpResponse("Public")
                    # return redirect('user_dashboard')
                else:
                    return redirect('logout')
            except:
                return redirect('logout')
        else:
            return redirect('logout')

class AdminDashboard(View):
    def get(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            admin = Account.objects.get(user=user)
            organizers = Account.objects.filter(type='organizer').count()
            students = Account.objects.filter(type='student').count()
            event = Event.objects.all()
            id = []
            for i in event:
                if i.last_date > datetime.datetime.now :
                    id.append(i.id)
            active_events=event.exclude(id__in=id).count()      
            context = {'account': admin,'organizers':organizers,'students':students,'event':event,'active_events':active_events}
            return render(request,'admin/dashboard.html', context)
        else:
            return redirect('home')

class AdminList(View):
    def get(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            admins = Account.objects.filter(type='admin')
            print(admins)
            context = {'account': account,'admins': admins}
            return render(request,'admin/admin_list.html', context)
        else:
            return redirect('home')

class OrganizerList(View):
    def get(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            organizers = Account.objects.filter(type='organizer')
            context = {'account': account,'organizers': organizers}
            return render(request,'admin/organizer_list.html', context)
        else:
            return redirect('home')


class StudentList(View):
    def get(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            student = Account.objects.filter(type='organizer')
            context = {'account': account,'student': student}
            return render(request,'admin/student_list.html', context)
        else:
            return redirect('home')






