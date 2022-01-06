from django.urls import path
from . import views

# URL endpoints for app
urlpatterns = [
	path('',views.index)
]