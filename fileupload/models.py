from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.first_name)


class Customer(models.Model):

    class Sex(models.TextChoices):
        MALE = 'Male', _('male')
        FEMALE = 'Female', _('female')

    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(choices=Sex.choices, max_length=6)
    phone_number = models.CharField(max_length=11)
    auxiliary_phone_number = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.TextField(max_length=150, null=True, blank=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images/customers/')
    instagram = models.URLField(unique=True, null=True, blank=True)
    facebook = models.URLField(unique=True, null=True, blank=True)
    twitter = models.URLField(unique=True, null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.customer.username + ' | ' + str(self.phone_number)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

# Create your models here.
