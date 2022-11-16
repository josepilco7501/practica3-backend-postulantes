from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('postulantes',views.PostulantesView.as_view(), name='postulantes'),
    path('postulante/<int:postulante_id>', views.PostulanteDetailView.as_view())
]