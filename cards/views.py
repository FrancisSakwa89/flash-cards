from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import ProfileForm, NewcardForm
from .models import Card,Profile

# Create your views here.
def welcome(request):
  id = request.user.id
  return render(request, 'index.html')


def card(request):
  frank = request.user
  cards = Card.objects.all()
  return render(request, 'card.html',{'profile':frank,'cards':cards})


def newcard(request):
  frank = request.user.id
  current_username = request.user.username

  if request.method == 'POST':
    owner = request.user
    user = Card(user=owner)
    form = NewcardForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
    return redirect('card')

  else:
    form = NewcardForm()

  return render(request, 'newcard.html',{'form':form,'profile':frank})


@login_required(login_url='/accounts/login/')
def profile(request, id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)

  user = request.user
  

  cards = card.objects.filter(post=frank).order_by()
  cardcount=cards.count()


  return render(request, 'profile.html',{'profile':profile,'user':user,'cardcount':cardcount,'cards':cards})


def newprofile(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  if request.method == 'POST':
    instance = get_object_or_404(Profile, user=frank)
    form = ProfileForm(request.POST, request.FILES,instance=instance)
    if form.is_valid():
      form.save()

    return redirect('profile', frank)

  else:
    form = ProfileForm()

  return render(request, 'newprofile.html',{'form':form,'profile':profile})
