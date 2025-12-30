from django.urls import path
from .views import get_Expense,add_expense,expense_detail

urlpatterns = [
    path('',get_Expense,name="get_Expense"),
    path('add/',add_expense,name="add_expense"),
    path('<int:pk>',expense_detail,name="expense_detail"),
]


