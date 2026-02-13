from django.urls import path
from . import views

urlpatterns = [
    path("health", views.health),   # keep your health
    path("customers/<int:customer_id>", views.customer_get),
    path("customers", views.customer_put),
]
