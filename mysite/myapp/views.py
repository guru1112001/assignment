from django.shortcuts import render,redirect
from .models import Customer
from .forms import UserForm
# from django.contrib import messages
from django.views.generic import ListView


class HomePageView(ListView):
    queryset=Customer.objects.all()
    context_object_name='users'
    paginate_by=3
    template_name='myapp/customer/homepage.html'

def add_customer(request):
    form=UserForm()
    user=None
    if request.method=='POST':
        form=UserForm(data=request.POST)

        if form.is_valid():
            user=form.save()
    else:
        form=UserForm()
    return render(request,"myapp/customer/add_customer.html",{"form":form,
                                                              'user':user,})



