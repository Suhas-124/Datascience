from testapp.views import TipsPrediction
from django.urls import path

urlpatterns = [
    path('predict/',TipsPrediction.as_view(),name='tips')
]