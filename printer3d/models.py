from django.db import models

# Create your models here.
class Printer3D(models.Model):
    title = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField()
    thumb_img = models.ImageField(blank=True)
    detail_img = models.ImageField(blank=True)
    description = models.TextField(blank=True,null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    reservation_user_name = models.CharField(max_length=100,null=True,blank=True)
    reservation_user_address = models.CharField(max_length=100,null=True,blank=True)
    reservation_user_email = models.EmailField(max_length=100,null=True,blank=True)
    reservation_user_phone = models.CharField(max_length=100,null=True,blank=True)
    reservation_start_date = models.DateTimeField(blank=True, null=True)
    reservation_end_date = models.DateTimeField(blank=True, null=True)
    reservation_status = models.NullBooleanField(blank=True, null=True)

    def __str__(self):
        return self.title

class Reservation(models.Model):
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50)
    start = models.DateTimeField(blank=True, null=True)
    finish = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title



