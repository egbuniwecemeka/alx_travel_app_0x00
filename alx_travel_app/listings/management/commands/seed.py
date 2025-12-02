""" A seeder file that seeds, localizes and test fake data """

# When seeding a model(A) that has a relationship with another model(B),
# ensure that model(B) is seeded first
from django_seed import Seed
from django.db.models.base import ModelBase
from ...models import Listing, Booking, Review, User
from random import randint

# seeder uses table and column type to populate the Model with relevant data
# AttributError(field) - error state
# locale argument determine the regional/language of the fake data generated

class Command(ModelBase):
    help = 'Populate the database with models entity '

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder(locale='en_NG')

        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('No user, seed user'))
            return
        
        for i in range(10):
            Listing.objects.create(
                user=user,
                title='Sample listing {i}',
                description='Travel listing {i}',
                price=1000 * i
            )
        self.stdout.write(self.style.SUCCESS('Listing seeded successfully'))

# Testing in django environment
# python3 runtests.py
# python3 manage.py test django_seed
# Alternatively, seeding can be executed directly on the django shell
# python3 manage.py shell -> After implementing seeding logic -> Press Enter
