from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import employee
import datetime
from . import forms

# Create your views here.
def welcome(req):
    date = datetime.datetime.now()
    mydict ={'date_msg':date}
    # s= "<h1>Hello friend good evening</h1><by><p>now time is %s</p>" %date;
    # s = s+'<p>login here</p>' 
    # s = s+'<a href="http://localhost:8000/me/login/">Login </a>'
    # return HttpResponse(s);
    return render(req,'firstApp/wish.html',context = mydict)

def loginPage(request):
    return render(request,'firstApp/login.html')
   
def databs(req):
    if req.method =='GET':
        form = forms.login()
        emp_list = employee.objects.order_by('Name')
        my_dict ={'emp_list': emp_list,'form':form}
        return render(req,'firstApp/db.html',context =my_dict)
    if req.method == 'POST':
        form = forms.login(req.POST)
        if form.is_valid():
            print('Form validation success and printing info')
            print(form.cleaned_data['username'])
            return thankyou_view(req)

    #  emp_list = employee.objects.all()
    


def thankyou_view(req):
    return render(req,'firstApp/thankyou.html')