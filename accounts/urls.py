
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.AccountView.as_view(),name="account_list"),
    path('deposit', views.DepositAndWithdraw.as_view(),name="transection"),
    path('history', views.TransectionHistory.as_view(),name="history"),
]
