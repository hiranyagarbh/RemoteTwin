from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient

def dashboard_view(reqest, *args, **kwargs):
	patient_det_view = Patient.objects.all()
	pat_context = {
		'patient_det_view': patient_det_view,
	}
	return render(reqest, "dashboard.html", pat_context)

def pat_history_view(reqest, *args, **kwargs):
    return render(reqest, "pat_history.html", {})

def appt_online_view(reqest, *args, **kwargs):
    return render(reqest, "appt_online.html", {})

def appt_physical_view(reqest, *args, **kwargs):
    return render(reqest, "appt_physical.html", {}) 