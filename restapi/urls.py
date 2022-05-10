
from restapi import views
from django.urls import path, include

urlpatterns = [
    path("expenses/", views.ExpenseListCreate.as_view(), name="expense-list-create"),
    path(
        "expenses/<pk>",
        views.ExpenseRetrieveDelete.as_view(),
        name="expense-retrieve-delete",
    ),
]
