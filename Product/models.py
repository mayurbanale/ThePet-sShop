from django.db import models


class category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)

    def __str__(s):
        return s.name


class product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    img = models.ImageField(upload_to="images", default="")
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(s):
        return s.name
