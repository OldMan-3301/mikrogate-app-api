from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports emial instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Router(models.Model):
    """Device to bes used in a contract"""
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    available = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Antenna(models.Model):
    """Device to bes used in a contract"""
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    available = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Package(models.Model):
    """Package to be used in a contract"""
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    price = models.IntegerField()
    available = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Contract(models.Model):
    """Contract object"""

    CHOICES = (
        ('new', 'New'),
        ('done', 'Done'),
        ('in-progress', 'In-Progress'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
        ('expired', 'Expired'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    referral = models.CharField(max_length=255, blank=True)
    contract_no = models.CharField(max_length=15)
    organization = models.CharField(max_length=255, blank=True)
    contract_type = models.CharField(max_length=255, blank=True)
    poc_name = models.CharField(max_length=255)
    poc_number = models.CharField(max_length=100)
    poc_email = models.EmailField(blank=True)
    address = models.CharField(max_length=255)
    # packages = models.ManyToManyField('Package', blank=True)
    packages = models.CharField(max_length=255, null=True, default='')
    package_price = models.IntegerField(blank=True, default=0)
    # router = models.ManyToManyField('Router', blank=True)
    router = models.CharField(max_length=255, null=True, default='')
    # antenna = models.ManyToManyField('Antenna', blank=True)
    antenna = models.CharField(max_length=255, null=True, default='')
    # customerDevices = models.CharField(max_length=255, null=True, default='')
    rou_cond = models.CharField(max_length=255, blank=True)
    rou_dec = models.CharField(max_length=255, blank=True)
    rou_qty = models.IntegerField(blank=True, null=True)
    rou_amnt = models.IntegerField(blank=True, null=True)
    rou_lease_amnt = models.IntegerField(blank=True, default=0)
    rou_amnt_totl = models.IntegerField(blank=True, null=True)
    rou_collected = models.BooleanField(blank=True, null=True)
    ann_cond = models.CharField(max_length=255, blank=True)
    ann_dec = models.CharField(max_length=255, blank=True)
    ann_qty = models.IntegerField(blank=True, null=True)
    ann_amnt = models.IntegerField(blank=True, null=True)
    ann_lease_amnt = models.IntegerField(blank=True, default=0)
    ann_amnt_totl = models.IntegerField(blank=True, null=True)
    ann_collected = models.BooleanField(blank=True, null=True)
    cable = models.DecimalField(max_digits=20, blank=True, null=True, decimal_places=2)
    cable_cond = models.CharField(max_length=255, blank=True)
    cable_collected = models.BooleanField(blank=True, null=True)
    other_service = models.CharField(max_length=255, blank=True)
    other_dec = models.CharField(max_length=255, blank=True)
    other_pay_method = models.CharField(max_length=255, blank=True)
    other_qty = models.IntegerField(blank=True, null=True)
    other_price = models.IntegerField(blank=True, null=True)
    payment_total = models.IntegerField(blank=True, null=True)
    service_charge = models.IntegerField(blank=True, null=True)
    other_charges = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    grand_total = models.IntegerField(blank=True, null=True)
    curren = models.CharField(max_length=5, blank=True, default='AFN')
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices = CHOICES, default='pending')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.contract_no


class Log(models.Model):
    """Contract Log Object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    contract = models.CharField(max_length=255)
    log = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)