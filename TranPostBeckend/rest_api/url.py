from django.urls import path
from .import views
from .views import GetEmployeeView,GetEmployeeByPostView,GetNewOfficeWithBlock,CleanArray,GetNewOffice
from django.views.decorators.csrf import csrf_exempt

urlpatterns =[ 
    
    path('employee/', GetEmployeeView.as_view(), name='employee-list'),
    path('employee/search/', GetEmployeeByPostView.as_view(), name='employee-list'),
    path('employee/search/new', csrf_exempt(GetNewOfficeWithBlock.as_view()), name='New Office with block'),
    path('employee/newoffice/', GetNewOffice.as_view(), name='New Office block and office'),
    path('employee/clean/', CleanArray.as_view(), name='employee-list'),
]