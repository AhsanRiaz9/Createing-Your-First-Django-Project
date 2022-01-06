from django.urls import path
from . import views

# URL endpoints for app
urlpatterns = [
	path('',views.index),
	path('index/',views.index),
	path('features/',views.features),
	path('about/',views.about),	
]