# File: places/models.py

from django.db import models
from django.core.validators import RegexValidator


class Place(models.Model):
    st = models.CharField('State', max_length=2, validators=[RegexValidator(regex=r'^[A-Z]{2}$', 
                          message='State must be 2 capital letters', code=None)])
    city = models.CharField('City', max_length=60)
    lat = models.DecimalField('Latitude', max_digits=9, decimal_places=6)
    lng = models.DecimalField('Longitude', max_digits=9, decimal_places=6)
    popn = models.IntegerField('Population', default=0)
    
    def __unicode__(self):
        return u'%s, %s: lat %s, long %s, pop. %d' % (self.city, self.st, self.lat, self.lng, self.popn)

    class Meta:
        db_table = 'places_place'
