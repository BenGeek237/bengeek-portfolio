from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()  # ← Déjà présent
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    # AJOUTER CETTE LIGNE pour définir le queryset
    queryset = Post.objects.filter(status='published')
    
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status', 'slug']
    search_fields = ['title', 'excerpt', 'content']
    ordering_fields = ['published_date', 'views', 'title']
    
    # MODIFIER CETTE MÉTHODE pour qu'elle utilise self.queryset
    def get_queryset(self):
        queryset = self.queryset  # ← Utiliser le queryset de base
        category_slug = self.request.query_params.get('category', None)
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset
    
    @action(detail=True, methods=['post'])
    def increment_views(self, request, pk=None):
        post = self.get_object()
        post.increment_views()
        return Response({'views': post.views})