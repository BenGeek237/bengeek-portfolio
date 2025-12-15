from django.db import models
from django.utils import timezone

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Développement Web'),
        ('mobile', 'Développement Mobile'),
        ('ai', 'IA / Machine Learning'),
        ('design', 'Design UI/UX'),
        ('other', 'Autre'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    technologies = models.CharField(max_length=300, help_text="Séparé par des virgules")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]