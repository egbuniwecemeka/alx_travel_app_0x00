""" A seeder file that seeds, localizes and test fake data """

# When seeding a model(A) that has a relationship with another model(B),
# ensure that model(B) is seeded first
from django_seed import Seed
from ...models import Listing, Booking, Review
from random import randint

# seeder uses table and column type to populate the Model with relevant data
# AttributError(field) - error state
# locale argument determine the regional/language of the fake data generated
seeder = Seed.seeder(locale='en_NG')

seeder.add_entity(Listing, 3)
seeder.add_entity(Booking, 4)
seeder.add_entity(Review, 5)

# Populating a column by addition of 3rd argument
seeder.add_entity(Listing, 3, {
    'scores': lambda x: randint(0, 100),
    'email': lambda x: seeder.faker.email(),
})

# seeder.executes returns a list of Pks, indexed by class
inserted_data = seeder.execute()


# Testing in django environment
# python3 runtests.py
# python3 manage.py test django_seed
# Alternatively, seeding can be executed directly on the django shell
# python3 manage.py shell -> After implementing seeding logic -> Press Enter
