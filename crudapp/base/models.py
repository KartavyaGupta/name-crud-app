from django.db import models

class Member(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)

    def  __str__(self):
        return self.firstname +" "+ self.lastname