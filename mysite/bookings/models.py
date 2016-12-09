from django.core.urlresolvers import reverse
from django.db import models

import math

STATUS_CHOICES = (
	('i', 'In Progress'),
	('r', 'In Review'),
	('p', 'Published'),
)


class Booking(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	description = models.TextField()
	is_live = models.BooleanField(default=False)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='i')


	def __str__(self):
		return self.title


class Step(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	content = models.TextField(blank=True, default='')
	order = models.IntegerField(default=0)
	booking = models.ForeignKey(Booking)

	class Meta:
		ordering = ['order',]


	def __str__(self):
		return self.title


