from django.db import models
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from samothrace.apps.sites.models import Site


class InscriptionManager(models.Manager):
     def get_by_natural_key(self, inscription_id, inscription_name):
        return self.get(inscription_id=inscription_id, inscription_name=inscription_name )

     
class Inscription(models.Model):
    
    objects = InscriptionManager()

    inscription_id = models.CharField(max_length=10, primary_key=True, verbose_name="Inscription ID")
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255, blank=True)
    alt_name = models.CharField(max_length=255, blank=True)
    find_spot = models.ForeignKey(Site)
    start_date = models.IntegerField(max_length=4, blank=True, null=True)
    end_date = models.IntegerField(max_length=4, blank=True, null=True)
    date_info = models.CharField(max_length = 255, blank=True)
    picture = models.ImageField(upload_to='inscriptions', max_length=100, blank=True, null=True)
    inscription_text = models.TextField(blank=True)
    bibliography = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    dating_certainty = models.TextField(blank=True)
    start_date_CE = models.IntegerField(max_length=4, blank=True, null=True)
    end_date_CE = models.IntegerField(max_length=4, blank=True, null=True)
    sites_mentioned = models.ManyToManyField(Site, related_name ='sites_mentioned', through='ReferenceSite', blank=True, null=True)

    
    # generate natural key
    def natural_key(self):
        return self.source
    
    def __unicode__(self):
         return self.source
    
    class Meta:
        ordering = ['inscription_id']

# http://stackoverflow.com/questions/5372934/
@receiver(pre_delete, sender=Inscription)
def inscription_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.picture.delete(False)
        
        
# class ReferenceSiteManager(models.Manager):
#     def get_by_natural_key(self, site.id, site.name):
#         return self.get(site.id=site.id, site.name=site.name)

    
class ReferenceSite(models.Model):
    '''Sites referenced by an inscription'''

    objects = models.Manager()

    inscription = models.ForeignKey("Inscription")
    site = models.ForeignKey(Site)

    def natural_key(self):
        return (self.inscription.id, self.site.id)
    
    def __unicode__(self):
        return '%s %s' % (self.site.id, self.site.name)


    
