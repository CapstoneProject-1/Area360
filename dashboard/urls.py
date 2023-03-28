from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name="dashboard"),
    path('properties',views.propertydashboard, name="allproperties"),
    path('properties/addproperty',views.addproperty, name="addproperty"),
    path('properties/allproperties',views.allproperties, name="allproperties"),
]