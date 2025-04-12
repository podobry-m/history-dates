from django import forms
from .models import HistoricalEvent
from datetime import datetime
class HistoricalEventForm(forms.ModelForm):
    class Meta:
        model = HistoricalEvent
        fields = ['date', 'title']
        widgets = {
              'title': forms.Textarea(attrs={'style': "width:100%;", 'class': 'form-control'}),
              'date': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': datetime.now().year
            })
        }
