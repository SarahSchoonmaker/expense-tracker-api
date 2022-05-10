
from restapi import views
from django.urls import path, include

urlpatterns = [path("expenses/", views.ExpenseListCreate.as_view(), name="expense-list-create")]
