from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/',views.welcome),
    path('login/',views.loginPage),
    path('users/',views.databs),
    # path('wish/',views.thankyou_view),
]
