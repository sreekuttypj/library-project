from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.views.decorators.cache import cache_control
from django.contrib.auth import login,authenticate
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import stud_registration_tb,admin_registration_tb,books_tb

# Create your views here.

def home(request):
	return render(request,'index.html')
    
#Admin login
def admin_login(request):
    if request.method=='POST':
        username=request.POST['username']
        # print(username)
        password=request.POST['password']
        # print(password)
        chk=admin_registration_tb.objects.filter(username=username,password=password)
        print(chk)
        if chk:
            for x in chk:
                request.session['id']=x.id
                print("-----------success----------")
            return render(request,'admin_home.html')
        else:
            print("-----------------filed----------------")
            return render(request,'admin_login.html')
    else:
        print("-----------------error----------------")
        return render(request,'admin_login.html')

#Admin registration
def admin_reg(request):
    if request.method=='POST':
       username=request.POST['Username']
       email=request.POST['email']
       password1=request.POST['password1']
       password2=request.POST['password2']
       chk=admin_registration_tb.objects.all().filter(email=email)
       if chk:
           print('Email alraedy exist')
           return render(request,'admin_reg.html')
       else:
            a=admin_registration_tb(username=username,email=email,password=password1)
            a.save()
            print('user created')
            return redirect('/admin_login/')
    else:
        return render(request,'admin_reg.html')
#Admin home page.
def admin_home(request):
    return render(request,'admin_home.html')

#Student registration
def stud_reg(request):
    if request.method=='POST':
       username=request.POST['Username']
       email=request.POST['email']
       password1=request.POST['password1']
       password2=request.POST['password2']
       chk=stud_registration_tb.objects.all().filter(email=email)
       if chk:
           print('Email alraedy exist')
           return render(request,'stud_reg.html')
       else:
            a=stud_registration_tb(username=username,email=email,password=password1)
            a.save()
            print('user created')
            return redirect('/stud_login/')
    else:
        return render(request,'stud_reg.html')

#Student login
def stud_login(request):
    if request.method=='POST':
        username=request.POST['username']
        # print(username)
        password=request.POST['password']
        # print(password)
        chk=stud_registration_tb.objects.filter(username=username,password=password)
        print(chk)
        if chk:
            for x in chk:
                request.session['id']=x.id
                print("-----------success----------")
            return render(request,'stud_home.html')
        else:
            return render(request,'stud_login.html')
    else:
        print("-----------------error----------------")
        return render(request,'stud_login.html')


#student home page.
def stud_home(request):
    return render(request,'stud_home.html')
    
#Add books
def admin_add_book(request):
    if request.method=='POST':
       bookname=request.POST['bookname']
       author=request.POST['authorname']
       description=request.POST['description']
       file=request.POST['file']
       chk=books_tb.objects.all().filter(bookname=bookname,author=author)
       if chk:
           print('Entry alraedy exist')
           return render(request,'admin_add_book.html')
       else:
            a=books_tb(bookname=bookname,author=author,description=description,file=file)
            a.save()
            print('book')
            return redirect('/admin_home/')
    else:
        return render(request,'admin_add_book.html')

#view all added books
def admin_view_book(request):
    uv=books_tb.objects.all()
    context={'uv':uv}
    return render(request,'admin_view_book.html',context)

#Delete an entry
def delete_book(request,id):
    books_tb.objects.filter(id=id).delete()
    return redirect('/admin_view_book/')

#Update an entry
def update(request):
     return render(request,'update.html')
    

#view all books added by admin in student dashboard
def stud_view_book(request):
    uv=books_tb.objects.all()
    context={'uv':uv}
    return render(request,'stud_view_book.html',context)

#Logout
def Logout(request):
    auth.logout(request)
    return redirect('/')