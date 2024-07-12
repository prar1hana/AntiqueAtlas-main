from django.db import models

# Create your models here.
class Archi(models.Model):# one to many
    Name=models.CharField(max_length=300)
    def __str__(self):
        return self.Name

class Materials(models.Model):#many to many
    Name=models.CharField(max_length=300)
    def __str__(self):
        return self.Name

class Country(models.Model):
    Name=models.CharField(max_length=100)
    def __str__(self):
        return self.Name
    
class State(models.Model):
    Name=models.CharField(max_length=100)
    Country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='States')
    def __str__(self):
        return self.Name
class historical_data(models.Model):
    Name=models.CharField(max_length=250)
    Country=models.ForeignKey(Country,on_delete=models.SET_NULL,blank=True,null=True)
    State=models.ForeignKey(State,on_delete=models.SET_NULL,blank=True,null=True)
    
    Arch_style=models.ForeignKey(Archi,
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE,
                                  related_name='buildings')
    Constr_Mat=models.ManyToManyField(Materials,
                                      related_name='buildings',
                                      null=True,blank=True)
    Constr_Year=models.IntegerField()
    Description=models.TextField()
    Fact=models.TextField()
    view_360deg=models.URLField(max_length=1000)
    Im=models.ImageField(upload_to='Images',null=True,blank=True)
    Gmap=models.URLField(max_length=1000)
    #latitude = models.DecimalField(max_digits=9, decimal_places=6)
    #longitude = models.DecimalField(max_digits=9, decimal_places=6)

    # Add spatial indexes
    #coordinates = models.PointField(geography=True)

    def __str__(self):
        return self.Name
    
class Contacts(models.Model):
    Name=models.CharField(max_length=250)
    Email=models.EmailField()
    Comment=models.TextField()
    def __str__(self):
        return self.Name