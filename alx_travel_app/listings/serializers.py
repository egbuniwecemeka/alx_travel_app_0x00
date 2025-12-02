"""
    Serializers for conversion of Django models to JSON format,
    and validation and conversion of incoming client data to Python objects
"""
from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """Handles serialization of Listing instances to/from JSON """
    class Meta:
        model = Listing
        fields = '__all__'
    

class BookingSerializer(serializers.ModelSerializer):
    """Handles serialization of Booking instances to/from JSON """
    class Meta:
        model = Booking
        fields = '__all__'
