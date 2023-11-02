from django.db.models.base import post_save
from django.utils.translation.trans_real import receiver
from .models import Member
from baptis.models import Baptis
from klerus.models import Klerus


@receiver(post_save, sender=Member)
def update_member_if_baptis_parent(sender, instance, created, **kwargs):
    if not created:
        Member.objects.filter(
                baptis_parent_id=instance.id
                ).update(
                        baptis_parent=instance.__str__()
                        )
        '''
        baptisan = Baptis.objects.filter(baptis_parent=instance)
        for baptis in baptisan:
                Member.objects.filter(
                        id=baptis.member.id
                        ).update(
                                baptis_parent=instance.__str__()
                                )
        '''


@receiver(post_save, sender=Member)
def update_member_baptis_by_klerus(sender, instance, created, **kwargs):
    if not created:
        if instance.is_klerus:
            Member.objects.filter(
                    baptis_klerus_id=instance.id
                    ).update(
                        baptis_klerus=instance.__str__()
                        )
            '''
            klerus = Klerus.objects.get(member=instance)
            baptisan = Baptis.objects.filter(baptis_klerus=klerus)
            for baptis in baptisan:
                Member.objects.filter(
                        id=baptis.member.id
                        ).update(
                                baptis_klerus=klerus.__str__()
                                )
            '''

