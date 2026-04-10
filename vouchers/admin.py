from django.contrib import admin
from .models import Voucher

@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'discount', 'expiry_date', 'is_active')
    search_fields = ('title', 'code')
    list_filter = ('is_active', 'expiry_date')
