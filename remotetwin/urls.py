"""remotetwin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboard_view, pat_history_view, appt_online_view, appt_physical_view
from patientend.views import patient_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('patient_history/', pat_history_view, name='patient_history'),
    path('appointment_online/', appt_online_view, name='appointment_online'),
    path('appointment_physical/', appt_physical_view, name='appointment_physical'),
	# patient end
	path('patientend/', patient_create_view, name='patientend'),
]
