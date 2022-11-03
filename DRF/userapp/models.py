from django.db import models

from django.contrib.auth.models import Group

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from django.contrib.auth.models import GroupManager

ROLE = [
        ('admin','admin'),
        ('manager','manager'),
        ('staff','staff')
    ]



class UserManager(BaseUserManager):
    def create_user(self, email,username,phone,role, password=None,password2 = None):
      
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            phone = phone,
            role = role
    
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,phone,role, password=None):
     
        user = self.create_user(
            email,
            password=password,
            username = username,
            phone = phone,
            role = role
    
        )
        user.is_admin = True
        user.save(using=self._db)
        return user






class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 15)
    role = models.CharField(max_length = 20,choices = ROLE)
    
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','role','phone']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin       




# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    description = models.TextField()
    count = models.IntegerField()       