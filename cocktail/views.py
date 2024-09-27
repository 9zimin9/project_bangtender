from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Cocktail
from .serializers import CocktailListSerializer, CocktailDetailSerializer

# 칵테일 목록 조회 및 추가
class CocktailListCreateView(generics.ListCreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

# 칵테일 상세 조회, 수정 및 삭제
class CocktailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# 북마크 기능 (POST)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def bookmark_cocktail(request, pk):
    try:
        cocktail = Cocktail.objects.get(pk=pk)
    except Cocktail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if user in cocktail.bookmarked_by.all():
        cocktail.bookmarked_by.remove(user)
        bookmarked = False
    else:
        cocktail.bookmarked_by.add(user)
        bookmarked = True

    return Response({'bookmarked': bookmarked})