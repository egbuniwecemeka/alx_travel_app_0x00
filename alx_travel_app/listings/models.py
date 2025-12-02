from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from uuid import uuid4

# Create your models here.

class User(models.Model):
    """
        User model
        attributes: represent a database field,
        each class attribute maps to a db column
    """
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=40, unique=True,)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Listing(models.Model):
    """ Listing model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    price = models.IntegerField(validators=[MinValueValidator(3)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'listing'

    def __str__(self):
        return self.title

class Booking(models.Model):
    """ Booking model """
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')

    class  Meta:
        """ Prevent overlapping booking by the same user """
        constraints = [
            models.UniqueConstraint(
                fields= ['user', 'listing', 'start_date', 'end_date'],
                name = 'unique_booking_period'
            )
        ]
        db_table = 'booking'
    
    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError('End date must be greater than start date')

    def __str__(self):
        return f'Booking {self.user} - {self.listing}'


class Review(models.Model):
    """ Review Model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Validates a review per user per listing """
        constraints = [
            models.UniqueConstraint(
                fields = ['user', 'listing'],
                name = 'unique_user_review'
            )
        ]
        db_table = 'review'

    def __str__(self):
        return f'Review by {self.user} - {self.rating}/5'
