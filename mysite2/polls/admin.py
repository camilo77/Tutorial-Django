from django.contrib import admin
from models import *

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

#midificando apariencia del admin para las preguntas
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 					{'fields': ['question']}),
		('date information', 	{'fields': ['pub_date'], 'classes': ['collapse']})
	]
	# agregando respuestas a preguntas
	inlines = [ChoiceInline]
	# modificando que campos mostrar en las tablas
	list_display = ('id','question', 'pub_date', 'was_published_recently')
	# par filtrar y orden segun:
	list_filter = ['pub_date']
	search_field = ['question']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
