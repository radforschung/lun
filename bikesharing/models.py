from django.db import models
from django.conf import settings
from django.contrib.gis.db import models as geomodels

# Create your models here.

bike_availability_status_choices = (
	('DI', 'Disabled'),
	('IU', 'In Use'),
	('AV', 'Available')
)

bike_state_status_choices = (
	('US', 'Usable'),
	('BR', 'Broken'),
	('IR', 'In Repair'),
	('SA', 'Sensor Alert')
)

bike_type_choices = (
	('FR', 'Fahrrad'),
	('LR', 'Lastenrad'),
	('EB', 'E-Bike'),
)

class Bike(models.Model):
	bike_number = models.CharField(max_length=8)
	current_position = geomodels.PointField(default=None, null=True)
	availability_status = models.CharField(max_length=2, choices=bike_availability_status_choices, default='DI')
	state = models.CharField(max_length=2, choices=bike_state_status_choices, default='US')
	bike_type = models.CharField(max_length=2, choices=bike_type_choices, default='FR')
	
	def __str__(self):
		return self.bike_number

class Rent(models.Model):
	rent_start = models.DateTimeField()
	rent_end = models.DateTimeField()
	start_position = geomodels.PointField(default=None, null=True)
	end_position = geomodels.PointField(default=None, null=True)
	bike = models.ForeignKey('Bike', on_delete=models.PROTECT)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
