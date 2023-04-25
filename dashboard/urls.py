from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name="dashboard"),
    path('properties/addproperty',views.addproperty, name="addproperty"),
    path('properties/addproject',views.addproject, name="addproject"),
    path('properties/allproperties',views.allproperties, name="allproperties"),
    path('supervisor/',views.supervisordashboard, name="sdashboard"),
    path('supervisor/properties',views.property_verification, name="propertyverification"),
    path('supervisor/projects',views.project_verification, name="projectverification"),
]