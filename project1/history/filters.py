import django_filters
from django_filters import CharFilter
from .models import *
from django import forms
class searchfilter(django_filters.FilterSet):
    Name=CharFilter(field_name='Name',lookup_expr='icontains')
    Country = django_filters.ModelChoiceFilter(field_name='Country', queryset=Country.objects.all())
    State = django_filters.ModelChoiceFilter(field_name='State', queryset=State.objects.all())

    class Meta:
        model=historical_data
        fields=['Country',
                'State',
                'Arch_style',
                'Constr_Mat',
                'Constr_Year']
        
