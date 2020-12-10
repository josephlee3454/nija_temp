from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=15)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.name + " " + " " + self.city + " " + self.state


class Nija(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length= 20)
    dojo = models.ForeignKey(Dojo, related_name="nija", on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + "" + self.last_name + "" 