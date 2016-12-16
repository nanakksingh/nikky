from __future__ import unicode_literals

from django.db import models
from shortner.models import DockURL

# Create your models here.

class ClickEventManager(models.Manager):
	def create_event(self, instance):
		if isinstance(instance, DockURL):
			obj, created = self.get_or_create(dock_url=instance)
			obj.count += 1
			obj.save()
			return obj.count
		return None	



class ClickEvent(models.Model):
	dock_url = models.OneToOneField(DockURL)
	count = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)
