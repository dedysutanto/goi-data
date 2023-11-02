from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Parokia, Komox, MemberParokia
from member.models import Member


@receiver(post_save, sender=Parokia)
def update_member_parokia(sender, instance, created, **kwargs):
    if not created:
        Member.objects.filter(
                parokia_id=instance.id
                ).update(
                        parokia=instance.__str__()
                        )

@receiver(post_save, sender=Komox)
def update_member_komox(sender, instance, created, **kwargs):
    if not created:
        Member.objects.filter(
                komox_id=instance.id
                ).update(
                        komox=instance.__str__()
                        )

@receiver(post_save, sender=MemberParokia)
def update_member_parokia_komox(sender, instance, created, **kwargs):
    member = Member.objects.get(id=instance.member.id)

    if instance.parokia:
        member.parokia_id = instance.parokia.id
        member.parokia = instance.parokia.__str__()
    else:
        member.parokia_id = 0
        member.parokia = None

    if instance.komox:
        member.komox_id = instance.komox.id
        member.komox = instance.komox.__str__()
    else:
        member.komox_id = 0
        member.komox = None

    member.save()

@receiver(post_delete, sender=Parokia)
def delete_member_parokia(sender, instance, **kwargs):
    Member.objects.filter(
            parokia_id=instance.id
            ).update(
                parokia=None,
                parokia_id=0
                ) 

@receiver(post_delete, sender=Komox)
def delete_member_komox(sender, instance, **kwargs):
    Member.objects.filter(
            komox_id=instance.id
            ).update(
                komox=None,
                komox_id=0,
                ) 

