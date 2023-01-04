from django.urls import path
from . import views

urlpatterns = [
    path("", views.Wishlists.as_view()),
    path("<int:pk>/series/<int:series_pk>", views.WishlistToggle.as_view()),
]
