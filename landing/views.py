from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import ListView
from member.models  import Member
from baptis.models import Baptis
from nikah.models import Nikah
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
            members_list = Member.objects.filter(
                Q(name__icontains=query) | Q(baptis_name__icontains=query) | Q(jabatan_klerus__icontains=query)
            )

            #nikah_list = Nikah.objects.filter(
            #    Q(suami__name__icontains=query) | Q(istri__name__icontains=query)
            #        )

            #for nikah in nikah_list:
            #    print(nikah.suami)

            for i in range(len(members_list)):
                members_list[i].complete_name = members_list[i].__str__()

                try:
                    nikah = Nikah.objects.get(suami=members_list[i])
                    members_list[i].is_nikah = True
                    members_list[i].nikah_istri = nikah.istri.__str__()
                    members_list[i].nikah_number = nikah.number
                    members_list[i].nikah_date = nikah.nikah_date
                    members_list[i].nikah_klerus = nikah.nikah_klerus
                    members_list[i].nikah_parokia = nikah.parokia
                    #print(nikah.suami)

                except ObjectDoesNotExist:
                    members_list[i].is_nikah = False
                    members_list[i].nikah_istri = None
                    members_list[i].nikah_number = None
                    members_list[i].nikah_date = None
                    members_list[i].nikah_klerus = None
                    members_list[i].nikah_parokia = None

            return members_list

            '''
            combined_list = Member.objects.none()
            for object_l in object_list:
                combine_list = combined_list | object_l
                if object_l.kepala_keluarga:
                    family = Anggota.objects.filter(nama_kepala_keluarga=object_l.nama_kepala_keluarga)
                    combined_list = combined_list | family

            return combined_list
            '''
