from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
	question = models.CharField('Pregunta', max_length = 200)
	pub_date = models.DateTimeField('Fecha de publicacion')

	def __unicode__(self):
		return self.question

	def __str__(self):
		return self.question

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = 'true'
	was_published_recently.short_description = 'published rencently?'
	


class Choice(models.Model):
	question = models.ForeignKey(Poll)
	choice_text = models.CharField('Opcion',max_length = 200)
	votes = models.IntegerField('No. votos',default = 0)

	def __unicode__(self):
		return self.choice_text

	def __str__(self):
		return self.choice_text