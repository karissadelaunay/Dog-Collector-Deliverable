from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/<int:dog_id>/add_exercise/', views.add_exercise, name='add_exercise'),
    path('dogs/<int:dog_id>/assoc_outfit/<int:outfit_id>/', views.assoc_outfit, name='assoc_outfit'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('outfits/', views.OutfitList.as_view(), name='outfits_index'),
    path('outfits/<int:pk>/', views.OutfitDetail.as_view(), name='outfits_detail'),
    path('outfits/create/', views.OutfitCreate.as_view(), name='outfits_create'),
    path('outfits/<int:pk>/update/', views.OutfitUpdate.as_view(), name='outfits_update'),
    path('outfits/<int:pk>/delete/', views.OutfitDelete.as_view(), name='outfits_delete'),
]