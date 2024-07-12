from django.forms import ModelForm
from .models import *
class Contactform(ModelForm):
    class Meta:
        model=Contacts
        fields='__all__'


        