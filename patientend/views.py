from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .form import PatientForm

    
def patient_create_view(request):
	form = PatientForm(request.POST or None)
	if form.is_valid():
		form.save()
	
	context = {'form': form}
		
	return render(request, "patientend/index.html", context)
