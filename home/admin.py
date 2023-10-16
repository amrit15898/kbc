from django.contrib import admin
from .models import *
from django import forms
# Register your models here.
class AnswersForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = '__all__'

AnswersFormSet = forms.inlineformset_factory(Questiom, Answers, form=AnswersForm, extra=4, can_delete=False)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswersFormSet]

admin.site.register(Questiom, QuestionAdmin)