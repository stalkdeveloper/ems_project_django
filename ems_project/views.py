from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, world! This is the home page.")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')