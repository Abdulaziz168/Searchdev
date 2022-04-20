from pyexpat import model
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'special'})

    class Meta:
        model = Project
        fields = ['title', 'description','demo_link','source_link','tag']