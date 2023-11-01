from django.db.models.base import post_save
from django.utils.translation.trans_real import receiver
from .models import Baptis
from member.models import Member


@receiver(post_save, sender=Baptis)
def update_member(sender, instance, created, **kwargs):
    member = Member.objects.get(id=instance.member.id)
    member.baptis_number = instance.number
    member.baptis_klerus = instance.baptis_klerus.__str__()
    member.baptis_parent = instance.baptis_parent.__str__()
    member.baptis_name = instance.baptis_name
    member.baptis_date = instance.baptis_date
    member.baptis_anniversary = instance.baptis_anniversary
    member.save()

