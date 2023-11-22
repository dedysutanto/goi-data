#from django.db.models.base import post_save, post_delete
from django.db.models.signals import post_save, post_delete
from django.utils.translation.trans_real import receiver
from parokia.models import MemberParokia
from .models import Baptis
from member.models import Member
from klerus.models import Klerus


@receiver(post_save, sender=Baptis)
def update_member(sender, instance, created, **kwargs):
    '''
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
    member.is_baptis = True
    member.baptis_number = instance.number
    member.baptis_name = instance.baptis_name
    member.baptis_date = instance.baptis_date
    member.baptis_anniversary = instance.baptis_anniversary

    if instance.baptis_klerus is not None:
        member.baptis_klerus_id = instance.baptis_klerus.id
        #klerus = Klerus.objects.get(id=instance.baptis_klerus.id)
        member.baptis_klerus = instance.baptis_klerus.__str__()
        #member.baptis_klerus = klerus.__str__()
        print('{} {}'.format(instance.baptis_klerus.id, instance.baptis_klerus.__str__()))
    else:
        member.baptis_klerus_id = 0
        member.baptis_klerus = None

    if instance.baptis_parent is not None:
        member.baptis_parent_id = instance.baptis_parent.id
        member.baptis_parent = instance.baptis_parent.__str__()
    else:
        member.baptis_parent_id = 0
        member.baptis_parent = None

    if instance.parokia is not None:
        member.parokia_id = instance.parokia.id
        member.parokia = instance.parokia.__str__()
    else:
        member.parokia_id = 0
        member.parokia = None

    if instance.komox is not None:
        member.komox_id = instance.komox.id
        member.komox = instance.komox.__str__()
    else:
        member.komox_id = 0
        member.komox = None

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
'''

@receiver(post_save, sender=Baptis)
def create_memberparokia(sender, instance, created, **kwargs):
    if created:
        try:
            MemberParokia.objects.create(
                member=instance.member,
                parokia=instance.parokia,
                komox=instance.komox
                )
        except:
            pass


@receiver(post_delete, sender=Baptis)
def clean_member_baptis(sender, instance, **kwargs):
    Member.objects.filter(
            id=instance.member.id
            ).update(
                is_baptis=False,
                baptis_number=None,
                baptis_klerus=None,
                baptis_parent=None,
                baptis_klerus_id=0,
                baptis_parent_id=0,
                baptis_name=None,
                baptis_date=None,
                baptis_anniversary=None,
                    )

