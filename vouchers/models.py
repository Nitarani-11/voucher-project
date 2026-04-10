from django.db import models

class Voucher(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.IntegerField()  # percentage
    code = models.CharField(max_length=50, unique=True)
    expiry_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
