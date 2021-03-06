from django.db import models
from django.contrib.auth.models import User

# Create your models here.

gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

states = (
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal')
    )


user_type=(
    ('admin','admin'),
    ('student','student'),
)

approval_choices=(
    ('2','Pending'),
    ('1','Approved'),
    ('3','Rejected')
)


class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200,null=True, blank=True)
    KTUID = models.CharField(max_length=250,null=True, blank=True)
    department = models.CharField(max_length=250,null=True, blank=True)
    year = models.CharField(max_length=4,null=True, blank=True)
    mob = models.CharField(max_length=10)
    sex = models.CharField(max_length=10,choices=gender,default='Male')
    house = models.CharField(max_length=100,null=True, blank=True)
    street1 =models.CharField(max_length=100,null=True, blank=True)
    street2 =models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    district = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True,choices=states, blank=True)
    pin = models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=20,choices=user_type)
    approval = models.CharField(max_length=20,choices=approval_choices,default='Pending')
    profilepic = models.ImageField(upload_to='documents',null=True, blank=True,default='accounts/static/images/user3.png')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=250)
    entry_date = models.DateField()
    last_date = models.DateField()
    details = models.TextField()
    poster = models.ImageField(upload_to='poster',null=True, blank=True, default='accounts/static/assets/images/blog/blog02.jpg')

    def __str__(self):
        return self.name

class Entry(models.Model):
    student = models.ForeignKey(Account,on_delete=models.CASCADE,null=True, blank=True,limit_choices_to={'type':'student'})
    event = models.ForeignKey(Event,on_delete=models.CASCADE,null=True, blank=True)
    url = models.CharField(max_length=1500)
    status = models.CharField(max_length=150,choices=approval_choices,default='Pending')
    remarks = models.TextField(max_length=1000,null=True, blank=True)
    marked = models.BooleanField(default=False)

    def __str__(self):
        return ("%s_%s") % (self.student,self.event)

class Result(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    result = models.TextField()

class LiveEvent(models.Model):
    name = models.CharField(max_length=1500)
    url = models.CharField(max_length=1500)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



    





