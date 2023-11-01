from django.db.models.base import post_save
from django.utils.translation.trans_real import receiver
from .models import Baptis
from member.models import Member
from klerus.models import Klerus


@receiver(post_save, sender=Baptis)
def update_member(sender, instance, created, **kwargs):
    Member.objects.filter(
            id=instance.member.id
            ).update(
                is_baptis=True,
                baptis_number=instance.number,
                baptis_klerus=instance.baptis_klerus.__str__(),
                baptis_parent=instance.baptis_parent.__str__(),
                baptis_name=instance.baptis_name,
                baptis_date=instance.baptis_date,
                baptis_anniversary=instance.baptis_anniversary,
                    )
    '''
    member = Member.objects.get(id=instance.member.id)
    member.baptis_number = instance.number
    member.baptis_klerus = instance.baptis_klerus.__str__()
    member.baptis_parent = instance.baptis_parent.__str__()
    member.baptis_name = instance.baptis_name
    member.baptis_date = instance.baptis_date
    member.baptis_anniversary = instance.baptis_anniversary
    member.save()
    '''


@receiver(post_save, sender=Baptis)
def update_member_baptis_by_klerus(sender, instance, created, **kwargs):
    if not created:
        if instance.member.is_klerus:
            klerus = Klerus.objects.get(member=instance.member)
            baptisan = Baptis.objects.filter(baptis_klerus=klerus)
            for baptis in baptisan:
                Member.objects.filter(
                        id=baptis.member.id
                        ).update(
                                baptis_klerus=klerus.__str__()
                                )

