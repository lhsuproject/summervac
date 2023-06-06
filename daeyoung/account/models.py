from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, name, phone, hakbun, gisoo, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an userID')
        if not name:
            raise ValueError('Users must have an name')
        if not phone:
            raise ValueError('Users must have an phone')
        if not hakbun:
            raise ValueError('Users must have an hakbun')
        if not gisoo:
            raise ValueError('Users must have an gisoo')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            name = name,
            phone = phone,
            hakbun = hakbun,
            gisoo = gisoo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user        
        
    def create_superuser(self, email, username, name, password, phone, hakbun, gisoo):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            name = name,
            password = password,
            phone = phone,
            hakbun = hakbun,
            gisoo = gisoo,
            
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=40,null=False, blank=False,default=True)
    phone =  models.CharField(max_length=40,blank=False,null=False,default=True)
    hackbun = models.CharField(max_length=40, blank=False,null=False,default=True)
    gisoo = models.CharField(max_length=40,blank=False,null=False,default=True)
    create_at = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)     
    
    objects = MyAccountManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','phone','hakbun','gisoo']
    #  USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username','name']
    
    
    def __str__(self):
        return self.name
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
        