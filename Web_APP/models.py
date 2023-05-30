from django.db import models

# Create your models here.
class Wheat_Disease(models.Model):
    name  = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField(max_length=3000, null=True)
    rem = models.TextField(max_length=3000, null=True)
    slug = models.CharField(max_length=48)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Rice_Disease(models.Model):
    name  = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField(max_length=3000, null=True)
    rem = models.TextField(max_length=3000, null=True)
    slug = models.CharField(max_length=48)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Potato_Disease(models.Model):
    name  = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField(max_length=3000, null=True)
    rem = models.TextField(max_length=3000, null=True)
    slug = models.CharField(max_length=48)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Groundnut_Disease(models.Model):
    name  = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField(max_length=3000, null=True)
    rem = models.TextField(max_length=3000, null=True)
    slug = models.CharField(max_length=48)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Pulses_Disease(models.Model):
    name  = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField(max_length=3000, null=True)
    rem = models.TextField(max_length=3000, null=True)
    slug = models.CharField(max_length=48)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Tomato_Disease(models.Model):
    name  = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField(max_length=3000, null=True)
    rem = models.TextField(max_length=3000, null=True)
    slug = models.CharField(max_length=48)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class ContactUS(models.Model):
    name  = models.CharField(max_length=100, null=True)
    number = models.IntegerField()
    subject  = models.CharField(max_length=100, null=True)
    message  = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.subject