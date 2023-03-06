from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

class Command(BaseCommand):
    help = 'Generates 100 random users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        emails = set()
        for i in range(100):
            email = fake.email()
            while email in emails:
                email = fake.email()
            emails.add(email)
            User.objects.create(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=email,
                password=fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully generated 100 random users'))

