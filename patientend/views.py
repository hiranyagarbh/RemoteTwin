from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient, Prognosis

def patientend_view(reqest, *args, **kwargs):
    return render(reqest, "patientend/index.html", {})

def create_prognosis(request):
	if request.method == 'POST':
		if request.POST.get('pat_aadhaar_number') and request.POST.get('pat_name') and request.POST.get('pat_age') and request.POST.get('pat_contact'):
			post = POST()
			post.aadhaar_id = request.POST.get('pat_aadhaar_number')
			post.name = request.POST.get('patient_name')
			post.age = request.POST.get('pat_age')
			post.gender = request.POST.get('pat_gender') # not required
			post.contact = request.POST.get('pat_contact')
			post.address = request.POST.get('pat_address') # not required
			post.problem_description = request.POST.get('problem_desc') # not required
			post.save()
			return render(request, "patientend/success.html")
		else:
			return render(request,"patientend/error.html")
