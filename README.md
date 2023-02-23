Car Rental System

This is a web application that allows customers to rent cars from different locations. It includes models for employers, customers, locations, cars, and reservations.

The app is built using Django Rest Framework (DRF) and SQLite database. The app consists of various models, including Car, Customer, Employer, Location, Reservation, and Rental, which are used to store data related to cars, customers, employers, locations, reservations, and rentals.

Models

Employer
The Employer model represents the company that owns the rental locations. It has the following fields:

name (CharField): The name of the employer.
user (OneToOneField)

Customer
The Customer model represents the person who rents the car. It has the following fields:

name (CharField): The first name of the customer.
phone (CharField): The phone number of the customer.
user (OneToOneField)

Location
The Location model represents the rental location. It has the following fields:

car (ManyToManyField)
city (CharField): The city of the location.
address (TextField): The address of the location.

Car

The Car model represents the car that can be rented. It has the following fields:

brand (ForeignKey): The brand of the car.
model (ForeignKey): The model of the car.
year (IntegerField): The year of the car.
color (CharField): The color of the car.
cost_per_day (DecimalField): The cost per day to rent the car.
is_available (BooleanField): Whether the car is available to rent.
fuel_type (ForeignKey): Fuel type of the car.
is_employer (ForeignKey): The employer of the car.

Reservation

The Reservation model represents a reservation for a car. It has the following fields:

customer (ForeignKey): The customer who made the reservation.
car (ForeignKey): The car that was reserved.
start_date (DateField): The start date of the reservation.
end_date (DateField): The end date of the reservation.
