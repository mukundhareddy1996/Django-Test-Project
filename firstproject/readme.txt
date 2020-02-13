username : mukundha
pwd : Mm@99499Mm@

--steps too follow

start a project
1) django-admin startproject project_name

create a application by using 
2) python manage.py application_name

3) add the application name in settings.py

4) define your own functions in views.py

5) create a folder in application level for appname_urls.py and add all the paths

6) Include the app level url path in project level urls.py using include.
from APPLICATION_NAME import views

7) create a template folder and static folder in project level 

8) inside the template folder, add the application_name folder and add all the html files

9) Indise the static folder, create CSS and IMAGES folder and inside which add the files accordingly.

10) include the {% load static %} in html all the html codes and for css "{%static "first_app/demo.css"%}"

11) Addd the paths in settings.py for TEMPLATE_DIR and add at 123 
STATICFILES_DIRS =[
    STATIC_DIR_PATH
]

12) For SQlite database the details are already provided in the settings.py file

13) to check run 
python manage.py shell

14) after which add the following commands
from django.db import connection
c = connection.cursor() 
If no error is there, we can see the database is connected
Quit()

15) In models.py of application level add the following code to create a table

class TABLE_NAME(models.Model):
    COLUMN_NAME1 = models.datatype( max_length =200)
    COLUMN_NAME2 = models.datatype

16) To generate the sql code run and execute the sql code
python manage.py makemigrations
python manage.py migrate

17) In admin.py file register and add a class to see the same in using
from APPLICATION_NAME.models import TABLE_NAME
admin.site.register(TABLE_NAME)

add this class too
class ADMIN_TABLENAME(admin.ModelAdmin):
    LIST_DISPLAY = ['ID','COL1','COL2']

admin.site.register(TABLE_NAME, ADMIN_TABLE_NAME)

18) TO login into admin URL htt://localhost:8000/admin
python manage.py createsuperuser
username:
mailid:
pwd:
conf pwd:

19) To get all the database details from a table in view.py do 
from APPLICATION_NAME.models import TABLE_NAME
and add the below code

emp_list = employee.objects.all()
where employee is the class name in models.py and the same we have imported.
my_dict = {'emp_list': emp_list}

Now send the same to template file

20) Use ninja2 template code to achive the emp_list in UI

21) create a forms.py file at application level and add a class similar to modules.py
from django import forms

class login(forms.Form):
    username = forms.CharField() --max_length is optional here
    password = forms.CharField()

22) In views.py file add this
from . import forms
form = forms.login()
and send the dorm to template using a dictionary or {'form':form}

23) In template folder use this
{{form}}

and to get the forma as a paragraph --> form.as_p

and add csrf_token, if not the django will throw error
{{form.as_p}}
{% csrf_token %} 

24) in <form>{{form.as_p}} </form>
views.py:
---------
if reuest.method ==post:                -- important as it will enter into this loop only after clicking the submit button
    form = forms.class_name(req.POST)
    if form.is_valid:
        print()
        print(form.cleaned_data['col1'])

cleaned_data --> which is a dictionary and the values which we provided are keys and user entered text will be the value
e.g. forms.cleaned_data['password']