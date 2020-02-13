import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')
import django
django.setup()

from firstApp.models import employee
from faker import Faker
from random import *
fake =Faker()

def phonenumbergen():
    d1 = randint(7,9)
    num =''+str(d1)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        # fdate = fake.date()
        # fcompany = fake.company()
        fname = fake.name()
        femail =fake.email()
        # fphonenumber = phonenumbergen()
        # ftitle = fake.random_element(elemnets =('project Manager','TeamLead','Software Engineer'))
        # feligibility = fake.random_element(elements =('B.tech','M.tech','Phd'))
        employee_record = employee.objects.get_or_create(Name =fname,email =femail)
        print(employee_record)
    
print(phonenumbergen())

