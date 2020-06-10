from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
def signup_view(request):
    if request.method =="POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the ueser in
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request,'account/signup.html', {'form':form})



def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        # if request.method:
        #     return redirect('articles:list')



    else:
        form = AuthenticationForm()
    return render(request,'account/login.html', {'form':form})

