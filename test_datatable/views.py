import datetime
from django.shortcuts import render
from django.views.generic import ListView
from .models import Studies
import random
from datetime import datetime
from django.db.models import Q


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def init_db(request):
    """
    База предоставляется уже предзаполненной, но в случае желания перехода
    на другую СУБД, можно раскомментировать код ниже и сгенерировать тестовые данные.
    """

    # Modalities.objects.all().delete()
    # modalities = [['CT', 'Computed Tomography'],
    #               ['MR', 'Magnetic Resonance'],
    #               ['PT', 'Positron emission tomography'],
    #               ['US', 'Ultrasound'],
    #               ['XA', 'X-Ray Angiography'],
    #               ['MG', 'Mammography'],
    #               ['CR', 'Computed Radiography'],
    #               ['AS', 'Angioscopy'],
    #               ['DX', 'Digital Radiography'],
    #               ['EC', 'Echocardiography']]
    # for modality in modalities:
    #     modality_obj = Modalities()
    #     modality_obj.short_code = modality[0]
    #     modality_obj.name = modality[1]
    #     modality_obj.save()
    # for i in range(100000):
    #     study_obj = Studies()
    #     study_obj.patient_fio = names.get_full_name()
    #     study_obj.patient_birthdate = random_date(datetime.datetime(2000, 1, 1, 0, 0, 0),
    #                                               datetime.datetime(2023, 1, 1, 0, 0, 0))
    #     study_obj.study_date = random_date(datetime.datetime(2023, 1, 1, 0, 0, 0),
    #                                        datetime.datetime(2023, 9, 1, 0, 0, 0))
    #     study_obj.study_uid = uuid.uuid4()
    #     random_modality_id = random.randint(1, 10)
    #     study_obj.study_modality = Modalities.objects.get(id=int(random_modality_id))
    #     study_obj.save()
    return render(request, 'test_datatable/init_db.html')


class ListDataVew(ListView):
    queryset = Studies.objects.all()
    template_name = 'test_datatable/list.html'
    context_object_name = 'data_list'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        # Сортировка
        sort = self.request.GET.get('sort')
        if sort:
            return queryset.order_by(sort)

        # Поиск
        search_fio = self.request.GET.get('search_fio', '')
        if search_fio:
            self.queryset = self.queryset.filter(patient_fio__icontains=search_fio)

        search_birth = self.request.GET.get('search_birth', '')
        if search_birth:
            self.queryset = self.queryset.filter(patient_birthdate__icontains=search_birth)

        search_uid = self.request.GET.get('search_uid', '')
        if search_uid:
            self.queryset = self.queryset.filter(study_uid__icontains=search_uid)

        search_date = self.request.GET.get('search_date', '')
        if search_date:
            self.queryset = self.queryset.filter(study_date__icontains=search_date)

        search_mod = self.request.GET.get('search_mod', '')
        if search_mod:
            self.queryset = self.queryset.filter(study_modality_id__name__icontains=search_mod)

        return self.queryset
