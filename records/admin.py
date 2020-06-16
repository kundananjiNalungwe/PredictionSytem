from django.contrib import admin
from .models import patient, patient_record, history

class patientModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "contact", "address"]
    list_filter = ["gender", "address"]
    search_fields = ["first_name", "last_name", "contact", "address"]
    class Meta:
        model = patient



class recordModelAdmin(admin.ModelAdmin):
    list_filter = ["outcome"]
    search_fields = ["patient"]
    class Meta:
        model = patient_record



class historyModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "submit_date", "updated"]
    list_filter = ["submit_date", "updated"]
    search_fields = ["patient_record"]
    class Meta:
        model = history


# Register your models here.
admin.site.register(patient, patientModelAdmin)
admin.site.register(patient_record, recordModelAdmin)
admin.site.register(history, historyModelAdmin)