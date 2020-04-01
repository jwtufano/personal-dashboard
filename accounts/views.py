from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("dashboard:dashboard"))
    return render(request, 'accounts/home.html')

# TODO redirect to dashboard
def logout_user(request):
    logout(request)
    return redirect('home')
