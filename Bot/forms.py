from django import forms
from .models import Bot

class BotForm(forms.Form):
    model = forms.ChoiceField(choices=Bot.MODEL_CHOICES, label="Model")
    prompt_text = forms.CharField(widget=forms.Textarea, label="System Prompt")

    def save(self):
        Bot(
            model=self.cleaned_data['model'],
            prompt_text=self.cleaned_data['prompt_text']
        ).save()
