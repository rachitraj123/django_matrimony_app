from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings


fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.
class Religion(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class sect(models.Model):
    name = models.CharField(max_length = 100)
    religion = models.ForeignKey(Religion, on_delete = models.CASCADE, related_name = "sects")
    
    def __str__(self):
        return self.name

class Caste(models.Model):
    caste = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.caste

class Hobbies(models.Model):
    name = models.CharField(max_length = 200)
    
    class meta:
        verbose_name_plural = "Hobbies"

    def __str__(self):
        return self.name

class father_profile(models.Model):
    name = models.CharField(max_length = 100)
    occupation = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    gender_choices = [('F', 'Female'), ('M', 'Male')]
    name = models.CharField(max_length=100, default="Unnamed")
    profile_picture = models.ImageField(null=True, blank=True, storage=fs)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    occupation = models.CharField(max_length=100, default="Not specified", null=True, blank = True)
    birth_date = models.DateField(null=True,blank = True)
    is_married = models.BooleanField(default=False)
    email = models.EmailField(max_length=254, null=True, unique=False)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='profiles', null = True)
    # caste = models.ForeignKey(Caste, on_delete=models.CASCADE, related_name='profiles', null = True)
    hobbies = models.ManyToManyField(Hobbies, related_name='profiles', null = True)
    father = models.OneToOneField(father_profile, on_delete=models.CASCADE ,related_name = "dependent" , null = True, blank = True)

    def save(self, *args, **kwargs):
        print(f"Data Saved for {self.name}")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
