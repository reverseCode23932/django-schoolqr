from django.db import models

class User(models.Model):
    name = models.CharField(blank=False,
                            max_length=50)
    user_class = models.CharField(blank=False,
                                  max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def get_url(self):
        return f"{self.id}"
        
    def __str__(self):
        return self.name