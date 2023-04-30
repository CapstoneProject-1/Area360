from django.db import models
from django.contrib.auth.models import User

from marketplace.models import Profile

# from marketplace.models import Profile

# Create your models here.

class Property_type(models.Model):
    property_type = models.CharField(max_length=30)

    def __str__(self):
        return self.property_type


class Property(models.Model):
    type = (
        ('Rent', 'Rent'),
        ('Sell', 'Sell'),
    )
    posting_as_a = (
        ('Full House', 'Full House'),
        ('On sharing basis', 'On sharing basis'),
    )
    age_of_construction = (
        ('less than 5 years', 'less than 5 years'),
        ('5 to 10 years', '5 to 10 years'),
        ('10 to 20 years', '10 to 20 years'),
        ('More than 20', 'More than 20'),
    )
    furnished = (
        ('Full Furnished', 'Full Furnished'),
        ('No Furnished', 'No Furnished'),
    )
    user_seller = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    property_purpose = models.CharField(max_length=10, choices=type)
    property_type = models.CharField(max_length=50)
    property_posting = models.CharField(max_length=30, choices=posting_as_a, default="On sharing basis", null=True, blank=True)
    property_address = models.CharField(max_length=200)
    property_state = models.CharField(max_length=100)
    property_city = models.CharField(max_length=100)
    # property_floor_no = models.IntegerField(null=True, blank=True)
    # property_area = models.IntegerField(null=True, blank=True)
    property_age_of_construction = models.CharField(
        max_length=100, choices=age_of_construction, null=True, blank=True)
    # property_floors_allowed_for_construction = models.IntegerField(blank=True)
    # property_no_of_open_sides = models.IntegerField(null=True, blank=True)
    property_bountry_wall = models.CharField(
        max_length=20, null=True, blank=True)
    property_furnished_status = models.CharField(
        max_length=50, choices=furnished, null=True, blank=True, default="No Furnished")
    # property_monthly_rent = models.IntegerField(null=True, blank=True)
    # property_maintenance_charges = models.IntegerField(null=True, blank=True)
    # property_price = models.IntegerField(null=True, blank=True)
    # property_booking_price = models.IntegerField(null=True, blank=True)
    dynamic_fields = models.JSONField(default=None)
    is_verified = models.BooleanField(default=False)
    property_no = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.property_type


class Property_image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="images/")
    image2 = models.ImageField(upload_to="images/", default="")
    image3 = models.ImageField(upload_to="images/", default="")
    image4 = models.ImageField(upload_to="images/", default="")
    image5 = models.ImageField(upload_to="images/", default="")
    slug = models.SlugField(unique=True)


class Project(models.Model):
    furnished = (
        ('Full Furnished', 'Full Furnished'),
        ('No Furnished', 'No Furnished'),
    )

    builder = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    projectname = models.CharField(max_length=100, blank=True, null=True)
    property_type = models.CharField(max_length=50)
    property_address = models.CharField(max_length=200)
    property_state = models.CharField(max_length=100)
    property_city = models.CharField(max_length=100)
    dynamic_fields = models.JSONField(default=None)
    property_furnished_status = models.CharField(max_length=50, choices=furnished, null=True, blank=True, default="No Furnished")
    is_verified = models.BooleanField(default=False)
    image1 = models.ImageField(upload_to="images/")
    image2 = models.ImageField(upload_to="images/", default="")
    image3 = models.ImageField(upload_to="images/", default="")
    image4 = models.ImageField(upload_to="images/", default="")
    image5 = models.ImageField(upload_to="images/", default="")
    booklet = models.FileField(upload_to="booklet/", default="")
    companyname = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    




