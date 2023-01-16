from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
# class Portfolio(models.Model):
#     class Meta():
#         db_table = 'portfolio'

#     name = models.CharField(
#         'Name',db_index=True,default='Alex',max_length=15
#     )

class About_slide_photo(models.Model):
  name = models.CharField(
    'Name', db_index=True, default='', max_length=15
  )
  image = CloudinaryField('image',default="")