from django.db import models

# Create your models here.
class Thought(models.Model):
    negative = models.CharField(max_length=200, unique=True)
    positive = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return '''
                Negative: {}
                Positive: {}
               '''.format(self.negative, self.positive)