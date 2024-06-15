from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # ... другие поля ...

    def __str__(self):
        return self.title