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
from .forms import *
# Create your views here.

class IndexView(View):
    def get(self, request):
        events = Event.objects.all()
        try:
            user = request.user
            context={'user': user,'events': events}
        except:
            context = {'events': events}
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


class PasswordChangeView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated: 
            form = PasswordChangeForm(user=user)
            user = request.user
            account = Account.objects.get(user=user)
            context = {'form': form, 'account': account}
            return render(request,'common/password_change.html',context)
        else:
            return redirect('logout')

    def poster(self, request):
        user = request.user
        if user.is_authenticated: 
            form = PasswordChangeForm(request.POST,user=user)
            user = request.user
            account = Account.objects.get(user=user)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                context = {'form': form, 'account': account}
                return render(request,'common/password_change.html',context)
        else:
            return redirect('home')
                



class Home(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                u = Account.objects.get(user=user)
                if u.type == 'admin':
                    return redirect('admin_dashboard')
                    # return HttpResponse("Admin Dashboard")
                elif u.type == 'student':
                    # return HttpResponse("Student")
                    return redirect('student_dashboard')
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
            admins = Account.objects.filter(type='admin').count()
            students = Account.objects.filter(type='student').count()
            # event = Event.objects.all()
            # id = []
            # for i in event:
            #     if i.last_date > datetime.datetime.now :
            #         id.append(i.id)
            # active_events=event.exclude(id__in=id).count()
            active_events = Event.objects.all().count()     
            context = {'account': admin,'admins':admins,'students':students,'active_events':active_events}
            return render(request,'admin/dashboard.html', context)
        else:
            return redirect('home')

class AdminList(View):
    def get(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            admins = Account.objects.filter(type='admin').exclude(user=user)
            context = {'account': account,'admins': admins}
            return render(request,'admin/admin_list.html', context)
        else:
            return redirect('home')


class StudentList(View):
    def get(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            student = Account.objects.filter(type='student')
            context = {'account': account,'student': student}
            return render(request,'admin/student_list.html', context)
        else:
            return redirect('home')


class AddEvent(View):
    def get(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            form = AddEventForm()
            context = {'account':account, 'form':form}
            return render(request, 'admin/add_event.html', context)
        else:
            return redirect('home')

    def post(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            form = AddEventForm(request.POST,request.FILES)
            if form.is_valid:
                form.save()
                return redirect('view_events')
            else:
                context = {'account':account, 'form':form}
            return render(request, 'admin/add_event.html', context)
        else:
            return redirect('home')


class ViewEvents(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            user = request.user
            account = Account.objects.get(user=user)
            event = Event.objects.all()
            context = {'account':account,'event': event}
            return render(request, 'common/events.html', context)
        else:
            return redirect('index')

class EditEvent(View):
    def get(self, request,id):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            event = Event.objects.get(id=id)
            form = AddEventForm(instance=event)
            context = {'account': account,'form': form,'event': event}
            return render(request, 'admin/edit_event.html', context)
        else:
            return redirect('home')

    def post(self, request,id):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            event = Event.objects.get(id=id)
            form = AddEventForm(request.POST,request.FILES,instance=event)
            if form.is_valid:
                form.save()
                return redirect('view_events')
            else:
                context = {'account': account,'form': form,'event':event}
                return render(request, 'admin/edit_event.html', context)
        else:
            return redirect('home')

class DeleteEvent(View):
    def get(self, request,id):
        x = AdminCheck(request)
        if x == True:
            event = Event.objects.get(id=id)
            event.delete()
            return redirect('view_events')
        else:
            return redirect('home')


class StudentSignUP(View):
    def get(self, request):
        form = StudentSignUpForm()
        dataform = DataForm()
        print(dataform)
        context = {'form': form,'dataform':dataform}
        return render(request, 'common/signup.html', context)
    
    def post(self, request):
        form = StudentSignUpForm(request.POST)
        dataform = DataForm(request.POST)
        msg = "Invalid registration id format"
        context = {'form': form,'dataform':dataform,'msg':msg}
        if form.is_valid() and dataform.is_valid():
            f = form.save(commit=False)
            username = f.username.upper()
            string1 = "TVE"
            string2 = "MCA"
            if string1 in username and string2 in username:
                f.save()
                d = dataform.save(commit=False)
                d.user = f
                d.type = 'student'
                d.save()
                return redirect('login')
            else:
                return render(request, 'common/signup.html', context)
        else:
            return render(request, 'common/signup.html', context)

class StudentDashboard(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            account = Account.objects.get(user=user)
            events = Event.objects.all().count()
            context = {'account':account,'active_events': events}
            return render(request, 'students/dashboard.html', context)
        else:
            return redirect('home')

class SubmitEntry(View):
    def get(self, request,id):
        user = request.user
        if user.is_authenticated:
            account = Account.objects.get(user=user)
            event = Event.objects.get(id=id)
            form = EntryForm()
            try:
                entry = Entry.objects.get(student=account, event=event)
                if entry:
                    return redirect('view_events')
            
            except:
                context = {'form': form, 'account': account,'event':event}
                return render(request,'students/submit.html', context)
        else:
            return redirect('home')

    def post(self, request,id):
        user = request.user
        if user.is_authenticated:
            account = Account.objects.get(user=user)
            event = Event.objects.get(id=id)
            form = EntryForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.student = account
                f.event = event
                f.status = '2'
                f.save()
                return redirect('view_events')
            else:
                context = {'form': form, 'account': account,'event':event}
                return render(request,'students/submit.html', context)
        else:
            return redirect('home')

class ViewEntries(View):
    def get(self, request,id):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            event = Event.objects.get(id=id)
            entry = Entry.objects.filter(event=event)
            context = {'account': account,'event':event,'entry':entry}
            return render(request, 'admin/entries.html', context)
        else:
            return redirect('home')

class PublishResult(View):
    def get(self, request,id):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            event = Event.objects.get(id=id)
            form = ResultForm()
            try:
                result = Result.objects.get(event=event)
                return redirect('view_events')
            except:
                context = {'account': account,'event':event,'form':form}
                return render(request, 'admin/publish_result.html', context)
        else:
            return redirect('home')

    def post(self, request,id):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            event = Event.objects.get(id=id)
            form = ResultForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.event = event
                f.save()
                return redirect('view_events')
            else:
                context = {'account': account,'event':event,'form':form}
                return render(request, 'admin/publish_result.html', context)
        else:
            return redirect('home')

class ViewResults(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            account = Account.objects.get(user=user)
            result = Result.objects.all()
            context = {'account':account,'result': result}
            return render(request, 'common/results.html', context)
        else:
            return redirect('home')


class ApproveEntry(View):
    def get(self, request,id):
        x= AdminCheck(request)
        if x == True:
            entry = Entry.objects.get(id=id)
            entry.status = '1'
            entry.save()
            event = Event.objects.get(id=entry.event.id)
            return redirect('view_entry',id=event.id )

class RejectEntry(View):
    def get(self, request,id):
        x= AdminCheck(request)
        if x == True:
            entry = Entry.objects.get(id=id)
            entry.status = '3'
            entry.save()
            event = Event.objects.get(id=entry.event.id)
            return redirect('view_entry',id=event.id )


class PublicEntryView(View):
    def get(self, request,id):
        event = Event.objects.get(id=id)
        entry = Entry.objects.filter(event=event,status='1')
        print(entry)
        context = {'event': event,'entry': entry}
        return render(request, 'common/public_entry.html', context)



class AddLiveEvent(View):
    def get(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            form = AddLivedEventForm()
            context = {'account':account, 'form':form}
            return render(request, 'admin/add_live_event.html', context)
        else:
            return redirect('home')

    def post(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            form = AddLivedEventForm(request.POST,request.FILES)
            if form.is_valid:
                form.save()
                return redirect('view_liveevents')
            else:
                context = {'account':account, 'form':form}
            return render(request, 'admin/add__live_event.html', context)
        else:
            return redirect('home')


class ViewLiveEvents(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            user = request.user
            account = Account.objects.get(user=user)
            event = LiveEvent.objects.all()
            context = {'account':account,'event': event}
            return render(request, 'common/live_events.html', context)
        else:
            return redirect('index')


class EditProfile(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            user = request.user
            account = Account.objects.get(user=user)
            form = EditStudentProfile(instance=account)
            context = {'account':account,'form':form}
            return render(request, 'students/edit_profile.html', context)
        else:
            return redirect('index')

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            user = request.user
            account = Account.objects.get(user=user)
            form = EditStudentProfile(request.POST,request.FILES,instance=account)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                context = {'account':account,'form':form}
                return render(request, 'students/edit_profile.html', context)
        else:
            return redirect('index')
                
class EditAdminProfile(View):
    def get(self, request):
        x = AdminCheck(request)
        if x == True:
            user = request.user
            account = Account.objects.get(user=user)
            form = EditStudentProfile(instance=account)
            context = {'account':account,'form':form}
            return render(request,'admin/edit_profile.html',context)
        else:
            return redirect('home')

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            user = request.user
            account = Account.objects.get(user=user)
            form = EditStudentProfile(request.POST,request.FILES,instance=account)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                context = {'account':account,'form':form}
                return render(request, 'admin/edit_profile.html', context)
        else:
            return redirect('index')












        



                




        
            

            






    













