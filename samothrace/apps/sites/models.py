from django.db import models
from tinymce import models as tinymce_models


class SiteManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

     
class Site(models.Model):
    '''Name of archeological site'''

    objects = SiteManager()

    site_id = models.CharField(max_length=10, primary_key=True, verbose_name="Site ID")
    name = models.CharField(max_length=255)
    mod_name = models.CharField(max_length=255, blank=True)
    alt_name = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    elevation = models.IntegerField(max_length=4, blank=True, null=True)
    pleiades_url = models.URLField(max_length=200, blank=True)
    perseus_url = models.URLField(max_length=200, blank=True)
    caption = models.CharField(max_length=255, blank=True)
    paragraph = tinymce_models.HTMLField(blank=True)
    natural_marker = models.CharField(max_length=255, blank=True)
    
    # generate natural key
    def natural_key(self):
        return (self.name)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

        
class MarkerManager(models.Manager):
    def get_by_natural_key(self, id):
        return self.get(id=id)

    
class Marker(models.Model):
    '''Physical markers found at sites'''

    objects = MarkerManager()

    marker_id = models.CharField(max_length=10, primary_key=True, verbose_name="Marker ID")
    type = models.CharField(max_length=255, blank=True)
    site = models.ForeignKey('Site')

    
class KoinaManager(models.Manager):
    def get_by_natural_key(self, id):
        return self.get(id=id)

    
class Koina(models.Model):
    '''federations linked to site'''

    objects = KoinaManager()

    koina_id = models.CharField(max_length=10, primary_key=True, verbose_name="Koina ID")
    site = models.ForeignKey('Site', null=True)
    inscription = models.ForeignKey('inscriptions.Inscription')
    member_count = models.IntegerField(max_length=4, blank=True, null=True)
    activities = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
            verbose_name_plural = 'Koina'




class Ancient_Sources(models.Model):
    '''historical references to site'''

    cityname = models.ForeignKey(Site, blank=True, db_column="name")
    author = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True, help_text="Text and section")
    author_date = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    citation_url = models.URLField(max_length=200, blank=True, null=True)
    bibliographic_reference = models.CharField(max_length=255, blank=True, null=True, help_text="Sources without available URL's")
    
    class Meta:
      verbose_name = 'Ancient Source'
      verbose_name_plural = 'Ancient Sources'
    
    def __unicode__(self):
        return '%s' % (self.author)