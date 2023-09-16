"""
Views for the Recipe API's
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):

    """View for managing recipe API's"""

    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permision_classes = [IsAuthenticated]

    def get_query_set(self):

        """Retrieve recipes for authenticated users"""

        return self.queryset.filter(user=self.request.user).order_by('-id')