from django.urls import path
from . import views

urlpatterns = [
    path("", views.Series_s.as_view()),
    path("drama", views.Series_Genre_Drama.as_view()),
    path("<int:pk>", views.Series_sDetail.as_view()),
    path("<int:pk>/reviews", views.Series_sReviews.as_view()),
]
