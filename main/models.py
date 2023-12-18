from django.db import models


# Model of databse object witch includes long (original) and short variants of every URL's
class Question(models.Model):
    original_url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10)
    creation_date = models.DateTimeField('creation date')
