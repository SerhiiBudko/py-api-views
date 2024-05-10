from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

routers = routers.DefaultRouter()
routers.register("cinema_halls", CinemaHallViewSet)
routers.register("movies", MovieViewSet)
urlpatterns = routers.urls

urlpatterns = [
    path("", include(routers.urls)),
    path("actor/", ActorList.as_view(), name="actor_list"),
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("genre/", GenreList.as_view(), name="genre_list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre_detail")
]

app_name = "cinema"
