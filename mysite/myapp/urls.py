from django.urls import path
from . import views
app_name="myapp"

urlpatterns=[
    path('',views.HomePageView.as_view(),name='homepage'),
    path('add/',views.add_customer,name='add_customer')

]