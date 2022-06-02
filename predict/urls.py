
from django.urls import path
from . import views


urlpatterns = [
    path('liver',views.liverPred,name='liverPred'),
    path('liverResult',views.liverPredResult,name='liverPredResult'),

    path('diabetes',views.diPred,name='diPred'),
    path('diabetesResult',views.diPredResult,name='diPredResult'),

    path('heart',views.heartPred,name='heartPred'),
    path('heartResult',views.heartPredResult,name='heartPredResult'),

    path('kidney',views.kidneyPred,name='kidneyPred'),
    path('kidneyResult',views.kidneyPredResult,name='kidneyPredResult'),

    path('cancer',views.cancerPred,name='cancerPred'),
    path('cancerresult',views.cancerPredResult,name='cancerPredResult'),

    path('backpred/<str:d_name>', views.backpred,name='backpred'),
    


]