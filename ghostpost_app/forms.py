from django import forms
from ghostpost_app.models import Post

class AddPostForm(forms.Form):
    boast_or_roast_choices = (
                (True, 'Boast'),
                (False, 'Roast')
            )
    boast_or_roast = forms.ChoiceField(choices = boast_or_roast_choices, label='Boast or Roast', initial='', widget=forms.Select(), required=True) # boast or roast setup
    text = forms.CharField(max_length=280)