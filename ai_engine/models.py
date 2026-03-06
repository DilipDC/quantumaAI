
from django.db import models

class AIInteraction(models.Model):
    user_prompt = models.TextField()
    ai_response = models.TextField()
    mode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_prompt[:50]
