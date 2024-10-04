from django import forms
from samothrace.apps.sites.models import Site
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'
        widgets = {
            'paragraph': forms.HTMLField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
        }
