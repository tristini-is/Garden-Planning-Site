from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),

    path ('planters/', views.PlanterListView.as_view(), name='planters'),
    path('planter/<int:pk>',views.PlanterDetailView.as_view(), name='planter-detail'),
    path('plant/<int:pk>', views.PlantDetailView.as_view(),
         name = 'plant-detail'),
   path('planter/<int:planter_id>/new_plant/', views.createPlant, name='create_plant'),
   path('planter/plant/<int:plant_id>/delete/', views.deletePlant, name='delete_plant'),
   path('plants/<int:plant_id>/update/', views.updatePlant, name='update_plant'),
   path('accounts/register/',views.registerPage, name = 'register'),

]