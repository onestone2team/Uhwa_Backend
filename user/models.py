from django.db import models

from address.models import AddressField
# from django.db.models.signals import pre_save
# from django.dispatch import receiver

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email')

        instance = self.model(
            email=email,
        )

        instance.set_password(password)
        instance.save(using=self._db)
        return instance

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        instance = self.create_user(
            email = email,
            password=password,
        )
        instance.is_admin = True
        instance.save(using=self._db)
        return instance


class Users(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',unique=True)
    password = models.CharField('비밀번호',max_length=30)
    profile = models.ImageField('프로필 사진',upload_to='%y/%m/', default='basic_profile/guest.png')
    profilename = models.CharField('회원이름',max_length=30,blank=True, default='-')
    # address = AddressField('배송지',max_length=100,blank=True, default='sth' )
    address = models.TextField('배송지',blank=True, default='-')
    phone = models.CharField('연락처',max_length=30,blank=True, default='-')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         self.profilename = self.user_id
    # super(Users,self).save(*args, **kwargs)
    
    # @receiver(pre_save, sender=Users)
    # def default_profilename(sender, instance, **kwargs):
    #  if not instance.profilename:
    #      instance.profilename = 'instance'+instance.user_id

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the instance have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the instance have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the instance a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin