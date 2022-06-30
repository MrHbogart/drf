from django.urls import path
from . import views

urlpatterns = [
    path("mixin/", views.ListProductMixin.as_view()),
    path("create/", views.CreateProductMixin.as_view()),
    path("products/<int:pk>/", views.DetailedProductMixin.as_view())
]