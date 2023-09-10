from django.contrib import admin

from test_datatable.models import Modalities, Studies


# admin.site.register(Question)


@admin.register(Modalities)
class ModalitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_code')
    search_fields = ('name',)


@admin.register(Studies)
class StudiesAdmin(admin.ModelAdmin):
    list_display = ('patient_fio', 'patient_birthdate', 'study_uid', 'study_date', 'study_modality')
    search_fields = ('patient_fio', 'study_modality__name__icontains')
