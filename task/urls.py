from django.urls import path
from task import views

urlpatterns = [
    path('tasks/', views.TaksListCreateAPIView.as_view()),
    path('tasks/<int:id_task>/', views.TaksDeteilAPIView.as_view()),
]