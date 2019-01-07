from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
  photo = models.ImageField(upload_to = 'photos/')
  bio = models.CharField(max_length=200)
  owner = models.ForeignKey(owner, on_delete=models.CASCADE,blank=True,null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()

  post_save.connect(save_user_profile, sender=User)

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()

class Card(models.Model):
  title = models.CharField(max_length=60)
  notes = models.TextField()
  owner = models.ForeignKey(owner, on_delete=models.CASCADE)
  pub_date = models.DateTimeField(auto_now_add=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

