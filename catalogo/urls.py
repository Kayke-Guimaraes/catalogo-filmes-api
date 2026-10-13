from rest_framework.routers import DefaultRouter

from .views import GeneroViewSet, FilmeViewSet


router = DefaultRouter()

router.register(
    r'generos',
    GeneroViewSet,
    basename='genero'
)

router.register(
    r'filmes',
    FilmeViewSet,
    basename='filme'
)

urlpatterns = router.urls