# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Patient(models.Model):
    aadhar_id = models.BigIntegerField(db_column='AADHAR_ID')
    patient_id = models.IntegerField(db_column='PATIENT_ID', primary_key=True)
    name = models.CharField(db_column='NAME', max_length=50)
    age = models.IntegerField(db_column='AGE')
    gender = models.CharField(db_column='GENDER', max_length=10)
    contact = models.CharField(db_column='CONTACT', max_length=15)
    address = models.CharField(db_column='ADDRESS', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PATIENT'


class Prognosis(models.Model):
    patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='PATIENT_ID')
    appointment_date = models.DateTimeField(db_column='APPOINTMENT_DATE')
    problem_description = models.CharField(db_column='PROBLEM_DESCRIPTION', max_length=200)
    number_of_days_suffering = models.IntegerField(db_column='NUMBER_OF_DAYS_SUFFERING')
    recommended_disease = models.CharField(db_column='RECOMMENDED_DISEASE', max_length=200, blank=True, null=True)
    bmi = models.FloatField(db_column='BMI', blank=True, null=True)
    ecg = models.CharField(db_column='ECG', max_length=200, blank=True, null=True)
    eeg = models.CharField(db_column='EEG', max_length=200, blank=True, null=True)
    eda = models.CharField(db_column='EDA', max_length=200, blank=True, null=True)
    lung_sound = models.CharField(db_column='LUNG_SOUND', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PROGNOSIS'


class Treatment(models.Model):
    patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='PATIENT_ID')
    timestamp = models.DateTimeField(db_column='TIMESTAMP')
    diagnosis = models.CharField(db_column='DIAGNOSIS', max_length=200, blank=True, null=True)
    prescribed_medicine = models.CharField(db_column='PRESCRIBED_MEDICINE', max_length=200, blank=True, null=True)
    comments = models.CharField(db_column='COMMENTS', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TREATMENT'
