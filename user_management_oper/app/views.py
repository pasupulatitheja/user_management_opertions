from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import User_register

# Create your views here.
def showadminwelcome(request):
    uname = request.POST['uname']
    upass = request.POST['upass']
    res = User_register.objects.get(Username=uname, password=upass)
    # request.session['name'] = res.uname
    if res:
        return render(request, 'badmin/adminwelcome.html')
    else:
        messages.error(request, "invalied Username/Password")
        return render(request,'login.html')
    # try:
    #
    #     res = User_register.objects.get(Username=uname,password=upass)
    #     request.session['name'] = res.uname
    #     return render(request, 'badmin/adminwelcome.html')
    # except:
    #     messages.error(request, "invalied Username/Password")
    #     return redirect('register')
    # uname = request.POST['uname']
    # upass = request.POST['upass']
    # if uname == 'admin' and upass == 'admin':
    #     request.session['name'] = uname
    #     return render(request,'badmin/adminwelcome.html')
    # else:
    #     messages.error(request, "invalied Username/Password")
    #     return redirect('adminloginpage')


def save_user_deatils(request):
    try:
        U_name = request.POST['uname']
        designation = request.POST['desig']
        U_pass = request.POST['upass']
        User_register(Username=U_name,desig=designation,password=U_pass).save()
        messages.success(request, "Register Succssfully")
        return redirect('register')
    except:
        messages.error(request, "Email-Id Already Used")
        return redirect('register')