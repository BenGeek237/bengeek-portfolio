from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project
from .serializers import ProjectSerializer

#ici c'est la classe pour afficher les projets 
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'featured']
    search_fields = ['title', 'description', 'technologies']
    ordering_fields = ['created_at', 'title']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        featured = self.request.query_params.get('featured', None)
        if featured == 'true':
            queryset = queryset.filter(featured=True)
        return queryset