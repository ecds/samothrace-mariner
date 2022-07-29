from django.db import models
from decimal import Decimal

from samothrace.apps.inscriptions.models import Inscription
from samothrace.apps.sites.models import Site


class IndividualManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Individual(models.Model):

    objects = IndividualManager()

    individual_id = models.CharField(max_length=10, primary_key=True, verbose_name='Individual ID')
    name = models.CharField(max_length=255, blank=True)
    patronym = models.CharField(max_length=255, blank=True)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, blank=True, null=True, help_text="The individual's city of origin", on_delete=models.CASCADE)
    # title data moved to Role table
    # title = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    site_origin = models.ForeignKey(Site, related_name='site_origin', blank=True, null=True, help_text="Inscription's city - can be left blank as long as the inscription is selected.", on_delete=models.CASCADE)

    def natural_key(self):
        return (self.name, self.name)

    def __unicode__(self):
        if self.name:
            if self.patronym:
                return '%s %s %s %s' % (self.individual_id, self.name, 'son of', self.patronym )
            else:
                return '%s %s' % (self.individual_id, self.name)
        else:
            return self.individual_id

    def __str__(self):
        if self.name:
            if self.patronym:
                return '%s %s %s %s' % (self.individual_id, self.name, 'son of', self.patronym )
            else:
                return '%s %s' % (self.individual_id, self.name)
        else:
            return self.individual_id

    class Meta:
        ordering = ['name', 'patronym']


class RoleManager(models.Manager):
    def get_by_natural_key(self, id):
        return self.get(id=id)


class Role(models.Model):
    '''People roles'''

    objects = RoleManager()

    role_id = models.CharField(max_length=10, primary_key=True, verbose_name="Role ID")
    individual = models.ForeignKey('Individual', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    certainty = models.DecimalField(max_digits=3, decimal_places=2, \
                verbose_name="certainty", default=Decimal(1.00), help_text="Enter a value between 0 and 1.")
    comments = models.TextField(blank=True)

    def natural_key(self):
        return self.title

    def __unicode__(self):
        return '%s %s' % (self.role_id, self.title)

    def __str__(self):
        return '%s %s' % (self.role_id, self.title)

    class Meta:
        ordering = ['title']


class PriesthoodManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Priesthood(models.Model):

    objects = PriesthoodManager()

    priesthood_id = models.CharField(max_length=255, primary_key=True, verbose_name="Priesthood ID")
    name = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    inscription = models.ManyToManyField(Inscription, blank=True)
    location = models.ForeignKey(Site, on_delete=models.CASCADE)
    deity_id = models.CharField(max_length=10, blank=True)
    deity = models.CharField(max_length=255, blank=True)
    duration = models.CharField(max_length=255, blank=True)
    att_honor = models.CharField(max_length=255, blank=True)
    cer_ritual = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    role = models.ForeignKey('Role', blank=True, null=True, on_delete=models.CASCADE) # temporarily optional

    def natural_key(self):
        return self.name

    def __unicode__(self):
        if self.name:
            return '%s %s' % (self.priesthood_id, self.name)
        else:
            return self.priesthood_id

    class Meta:
        ordering = ['name']
