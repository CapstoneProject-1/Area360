from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneno = models.CharField(max_length=10)
    otp = models.CharField(max_length=4, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    forgot_password_token = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    choices = (
        ('Buyer','Buyer'),
        ('Seller','Seller'),
        ('Builder','Builder'),
    )
    usertype = models.CharField(max_length=30, choices=choices, default='Buyer')

    def __str__ (self):
        return self.user.username