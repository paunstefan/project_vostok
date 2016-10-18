from django.db import models
import csv

class Flight(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length = 64)
    members = models.TextField()
    date = models.CharField(max_length = 8)
    country = models.CharField(max_length = 16)

    def __str__(self):
        return self.name

'''
# Imports database from .csv file 
with open(r'D:\Stefan\Programming\Web\Project Vostok\manned_flight.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		_, created = Flight.objects.get_or_create(
			year=row[0],
			name=row[1],
			members=row[2],
			date = row[3],
			country = row[4],
			)'''