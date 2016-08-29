from django.db import models
from tinymce import models as tinymce_models

from samothrace.apps.inscriptions.models import Inscription
from samothrace.apps.sites.models import Site


class Person(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    origin = models.ForeignKey(Site, null=True, blank=True)
    source = models.CharField(max_length=255, blank=True, null=True, choices=(('Apollonius of Rhodes', 'Apollonius of Rhodes'),('[Orpheus]','[Orpheus]'),('Valerius Flaccus','Valerius Flaccus')))
#    tribe = models.CharField(max_length=255, blank=True, null=True)

    def natural_key(self):
        return (self.name)

    def __unicode__(self):
        return self.name or u''

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'People'


class Stops(models.Model):
    place_of_stop = models.ForeignKey(Site, blank=True, related_name='stop')
    previous_place = models.ForeignKey(Site, blank=True, null=True, related_name='previous')
    next_place = models.ForeignKey(Site, blank=True, null=True, related_name='next')
    type_of_stop = models.CharField(max_length=255, blank=True, null=True, choices=(('direct', 'direct'),('indirect', 'indirect')))
    line_number = models.CharField(max_length=255, blank=True, null=True)
    crew = models.ManyToManyField('Person', blank=True, null=True, related_name='crew', help_text="People on the Ship Manifest at the time")
    ritual = models.CharField(max_length=255, blank=True, null=True)
    ritual_deity = models.CharField(max_length=255, blank=True, null=True)
    ritual_people = models.ManyToManyField('Person', blank=True, null=True, related_name='ritualpeople', help_text="People associated with the ritual")
    argonautica_edition = models.CharField(max_length=255, blank=True, null=True, choices=(('Apollonius of Rhodes', 'Apollonius of Rhodes'),('[Orpheus]','[Orpheus]'),('Valerius Flaccus','Valerius Flaccus')))

    def natural_key(self):
        return (self.line_number)

    def __unicode__(self):
        return '%s %s' % (self.line_number, self.type_of_stop) or u''

    class Meta:
        ordering = ['line_number']
        verbose_name = 'Sequence Stop'
        verbose_name_plural = 'Stops'




class Places_Referenced(models.Model):
    place_referenced = models.ForeignKey(Site, blank=True, related_name='ref')
    line_number = models.CharField(max_length=255, blank=True, null=True)
    type_of_reference = models.CharField(max_length=255, blank=True, null=True)
    referenced_by = models.ForeignKey('Person', blank=True, null=True, related_name='speaking', help_text="Person making the place reference")
    previous_place = models.ForeignKey(Site, blank=True, related_name='previous2')
    next_place = models.ForeignKey(Site, blank=True, related_name='next2')
    ritual = models.CharField(max_length=255, blank=True, null=True)
    ritual_deity = models.CharField(max_length=255, blank=True, null=True)
    ritual_people = models.ManyToManyField('Person', blank=True, null=True, related_name='ritualpeople2', help_text="People associated with the ritual")
    argonautica_edition = models.CharField(max_length=255, blank=True, null=True, choices=(('Apollonius of Rhodes', 'Apollonius of Rhodes'),('[Orpheus]','[Orpheus]'),('Valerius Flaccus','Valerius Flaccus')))

    def natural_key(self):
        return (self.line_number)

    def __unicode__(self):
        return '%s %s' % (self.line_number, self.type_of_reference) or u''

    class Meta:
        ordering = ['line_number']
        verbose_name = 'Place Referenced'
        verbose_name_plural = 'Places Referenced'
