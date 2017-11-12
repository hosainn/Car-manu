from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class CarModel(models.Model):
    model = models.CharField(max_length=63)



    def __str__(self):
        return '{}'.format(self.model)

    def get_absolute_url(self):
        return reverse('car_parts_create')


class CarParts(models.Model):
    carmodel = models.ForeignKey(CarModel)
    name = models.CharField(max_length=63)
    parts = models.IntegerField()
    level = models.IntegerField()



    class Meta:
        ordering = ['level','parts']

    def __str__(self):
        return '{}'.format(self.name)


    def get_absolute_url(self):
        return reverse('car_parts_create')



