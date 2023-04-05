from test_app.models import Company, Person
from django.db.models.signals import post_save
from django.dispatch import receiver
from test_app.models import CompanyProfile, PersonProfile

#create signals heare

@receiver(post_save, sender=Company)
def create_profile(sender, instance, created, **kwarg):
	if created:
		CompanyProfile.objects.create(Company=instance)

@receiver(post_save, sender=Company)
def save_profile(sender, instance, **kwargs):
	instance.CompanyProfile.save()
 
 
 
 
@receiver(post_save, sender=Person)
def create_profile(sender, instance, created, **kwarg):
	if created:
		PersonProfile.objects.create(Person=instance)

@receiver(post_save, sender=Person)
def save_profile(sender, instance, **kwargs):
	instance.PersonProfile.save()

