from django.urls import path
from .views import VoucherListView, VoucherCreateView, VoucherDetailView

urlpatterns = [
    path('', VoucherListView.as_view()),
    path('create/', VoucherCreateView.as_view()),
    path('<int:pk>/', VoucherDetailView.as_view()),
]