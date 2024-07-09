from django.urls import path
from .views import *

urlpatterns = [
    path('',CountryView.as_view(),name='country'),
    path('/<int:id>',CountryView.as_view(),name='country'),
    # path('Delete/<int:id>',Delete_view,name='Delete')
    
]