from django import forms
from django.contrib.auth.models import User

from records.models import patient, patient_record


class PatientForm(forms.ModelForm):

    class Meta:
        model = patient
        fields = ['first_name', 'last_name', 'gender', 'contact', 'address']


class PatientRecordForm(forms.ModelForm):

    class Meta:
        model = patient_record
        fields = ['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'diabetes_pedigree_function', 'age']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']