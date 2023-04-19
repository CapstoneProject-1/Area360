from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import requests
from django.contrib.auth.models import Group
from django.contrib import messages
from django.utils.crypto import get_random_string

from .models import *

# group_required decorator
def group_required(*group_names):
    def in_group(u):
        return (u.is_superuser or bool(u.groups.filter(name__in=group_names)))
    return user_passes_test(in_group)


def group(request):
    groups = request.user.groups.all()
    return groups



# Create your views here.
@login_required
@group_required('Seller', 'Builder')
def dashboard(request):
    profile = Profile.objects.get(user = request.user)
    total_properties = Property.objects.filter(user_seller = profile).count()
    verified_properties = Property.objects.filter(user_seller = profile, is_verified = True).count()
    groups = group(request)
    context = {"groups": groups, "total_properties": total_properties, "verified_properties": verified_properties}
    return render(request, 'dashboardComponents/maindashboard.html', context)

def addproperty(request):
    states_url = "https://api.countrystatecity.in/v1/countries/IN/states"
    cities_url = "https://api.countrystatecity.in/v1/countries/IN/cities"
    headers = {
        'X-CSCAPI-KEY': 'blhwU1g0VUZ4Wm1lck8zeTg5WjZIN1dvZ0JHR09NUmJrcjlTYzVRZw=='
    }
    states = requests.request("GET", states_url, headers=headers).json()
    cities = requests.request("GET", cities_url, headers=headers).json()

    property_type = Property_type.objects.all()

    groups = group(request)
    context = {"states": states, "cities": cities,
               "groups": groups, "property_type": property_type}

    if request.method == "POST":
        property_purpose = request.POST.get('sr')
        property_type = request.POST.get('property_type')
        posting = request.POST.get('posting')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        total_floors = request.POST.get('tf')
        floorno = request.POST.get('fn')
        area = request.POST.get('area')
        age_of_construction = request.POST.get('aoc')
        floors_allowed = request.POST.get('fafc')
        open_sides = request.POST.get('op')
        bountry_wall = request.POST.get('bw')
        furnished_status = request.POST.get('fs')
        monthly_rent = request.POST.get('mrent')
        maintenance_charges = request.POST.get('mc')
        price = request.POST.get('price')
        booking_price = request.POST.get('bprice')
       
        
        user = Profile.objects.get(user = request.user)
       
        property_obj = Property(
                                user_seller=user,
                                property_purpose=property_purpose,
                                property_type=property_type,
                                property_posting=posting,
                                property_state=state,
                                property_city=city,
                                # property_total_floors=total_floors,
                                # property_floor_no=floorno,
                                # property_area=area,
                                property_age_of_construction=age_of_construction,
                                # property_floors_allowed_for_construction=floors_allowed,
                                # property_no_of_open_sides=open_sides,
                                property_bountry_wall=bountry_wall,
                                property_furnished_status=furnished_status,
                                # property_monthly_rent=monthly_rent,
                                # property_maintenance_charges=maintenance_charges,
                                # property_price=price,
                                # property_booking_price=booking_price,
                                dynamic_fields={"property_total_floors": total_floors,
                                                "property_floor_no": floorno,
                                                "property_area": area,
                                                "property_floors_allowed_for_construction": floors_allowed,
                                                "property_no_of_open_sides": open_sides,
                                                "property_monthly_rent": monthly_rent,
                                                "property_maintenance_charges": maintenance_charges,
                                                "property_price": price,
                                                "property_booking_price": booking_price
                                                },
                                )
        

        property_obj.save()

        property_image1 = request.FILES['image1']
        property_image2 = request.FILES['image2']
        property_image3 = request.FILES['image3']
        property_image4 = request.FILES['image4']
        property_image5 = request.FILES['image5']
        slug = get_random_string(8,"0123456789n")

        image_obj = Property_image.objects.create(property=property_obj,
                                                   image1=property_image1,
                                                   image2=property_image2,
                                                   image3=property_image3,
                                                   image4=property_image4,
                                                   image5=property_image5,
                                                   slug = slug
                                                  )
        image_obj.save()
        # list1 = [property_image1,property_image2,property_image3,property_image4,property_image5]

        # for i in list1:
        #     image_obj = Property_image.objects.create(property= property_obj, image1 = i)
        #     image_obj.save()
        messages.success(request, 'Property successfuly added.')

    return render(request, 'dashboardComponents/addproperty.html', context)


def allproperties(request):
    profile = Profile.objects.get(user = request.user)
    properties  = Property.objects.filter(user_seller = profile)
    groups = group(request)
    context = {"groups": groups, "properties": properties}
    return render(request, 'dashboardComponents/allproperties.html', context)

