from django.db import models

class Bot(models.Model):
    MODEL_CHOICES = [
        ('Gemini', 'Gemini'),
        ('OpenAI', 'OpenAI'),
    ]
    
    aimodel = models.CharField(max_length=20, choices=MODEL_CHOICES, default='GEMINI')
    model_name = models.CharField(max_length=100, default='gemini-1.5-flash')
    description = models.TextField()
    prompt_text = models.TextField()

    def __str__(self):
        return f"{self.aimodel}: {self.prompt_text[:30]}..."
