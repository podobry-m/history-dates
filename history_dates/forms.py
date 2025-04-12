from django import forms
from .models import HistoricalEvent

class HistoricalEventForm(forms.ModelForm):
    class Meta:
        model = HistoricalEvent
        fields = ['date', 'title']
        widgets = {
              'title': forms.Textarea(attrs={'style': "width:100%;"}),
        }
