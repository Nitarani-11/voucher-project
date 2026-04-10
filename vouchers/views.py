from rest_framework import generics
from .models import Voucher
from .serializers import VoucherSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from django.utils.timezone import now


# All vouchers (USER)
class VoucherListView(generics.ListAPIView):
    queryset = Voucher.objects.filter(is_active=True, expiry_date__gt=now())
    serializer_class = VoucherSerializer
    permission_classes = [IsAuthenticated]


# Create voucher (ADMIN)
class VoucherCreateView(generics.CreateAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    permission_classes = [IsAuthenticated]


# Detail view
class VoucherDetailView(generics.RetrieveAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    permission_classes = [IsAuthenticated]

class IsAdminUserRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ADMIN'

class VoucherCreateView(generics.CreateAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]

