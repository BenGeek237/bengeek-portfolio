from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    technologies_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'description', 'short_description',
            'category', 'technologies', 'technologies_list',
            'image', 'github_url', 'live_url', 'featured',
            'created_at', 'updated_at'
        ]
    
    def get_technologies_list(self, obj):
        return obj.get_technologies_list()