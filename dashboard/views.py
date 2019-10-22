from django.shortcuts import render
from django.http import HttpResponse

def dashboard_view(reqest, *args, **kwargs):
    return render(reqest, "dashboard.html", {})

def pat_history_view(reqest, *args, **kwargs):
    return render(reqest, "pat_history.html", {})

def appt_online_view(reqest, *args, **kwargs):
    return render(reqest, "appt_online.html", {})

def appt_physical_view(reqest, *args, **kwargs):
    return render(reqest, "appt_physical.html", {})