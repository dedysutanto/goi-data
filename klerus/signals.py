from django.core.exceptions import ObjectDoesNotExist
from django.db.models.base import post_save
from django.utils.translation.trans_real import receiver
from .models import Klerus
from member.models import Member
from baptis.models import Baptis


@receiver(post_save, sender=Klerus)
def update_member(sender, instance, created, **kwargs):
    Member.objects.filter(
            id=instance.member.id
            ).update(
                    is_klerus=True,
                    jabatan_klerus=instance.jabatan.name
                    )
    '''
    member = Member.objects.get(id=instance.member.id)
    member.is_klerus = True
    member.jabatan_klerus = instance.jabatan_klerus
    member.save()
    '''

@receiver(post_save, sender=Klerus)
def update_member_baptis(sender, instance, created, **kwargs):
    if not created:
        try:
            members_baptis = Baptis.objects.filter(baptis_klerus=instance)
            for member_baptis in members_baptis:
                Member.objects.filter(
                    id=member_baptis.member.id
                    ).update(
                        baptis_klerus=instance.__str__()
                        )

        except ObjectDoesNotExist:
            pass

