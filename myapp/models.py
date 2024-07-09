from django.db import models
import uuid

# Create your models here.
class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4 , editable = False)
    
    class Meta:
        abstract = True
        
class Country(Base):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=10 , unique=True)
    flag = models.ImageField(upload_to ='flag')
    is_state_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.name
    
class State(Base):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)
    language = models.CharField(max_length = 200)
    population = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class City(Base):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    
    
        
    
    