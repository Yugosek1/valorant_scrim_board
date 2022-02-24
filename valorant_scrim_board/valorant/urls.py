from django.urls import path
from .views import (ScrimDetailView,
                    ScrimListView,
                    ScrimCreateFormView,
                    ScrimUpdateFormView,
                    ScrimDeleteView
                    )

urlpatterns = [
    path("", ScrimListView.as_view(), name="scrim_list"),
    path("detail/<int:pk>/", ScrimDetailView.as_view(), name="scrim_detail"),
    path("create/", ScrimCreateFormView.as_view(), name="scrim_create"),
    path("update/<int:pk>", ScrimUpdateFormView.as_view(), name="scrim_update"),
    path("delete/<int:pk>/", ScrimDeleteView.as_view(), name="scrim_delete"),

]