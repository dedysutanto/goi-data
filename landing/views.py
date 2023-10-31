from django.shortcuts import render
from django.views.generic import ListView
from member.models  import Member
from django.db.models import Q

def index(request):
    return render(request, 'landing/index.html')

class IndexView(ListView):
    model = Member
    template_name = 'landing/index.html'
    
    #queryset = Anggota.objects.filter(name__icontains='Dedy') # new

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            object_list = Member.objects.filter(
                Q(name__icontains=query) | Q(baptis_name__icontains=query) | Q(jabatan_klerus__icontains=query)
            )
            return object_list

            '''
            combined_list = Member.objects.none()
            for object_l in object_list:
                combine_list = combined_list | object_l
                if object_l.kepala_keluarga:
                    family = Anggota.objects.filter(nama_kepala_keluarga=object_l.nama_kepala_keluarga)
                    combined_list = combined_list | family

            return combined_list
            '''
