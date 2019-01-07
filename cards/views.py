from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import ProfileForm NewcardForm
# from .email import send_welcome_email
# from django.db.models import Avg
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializer import NeighbourhoodSerializer, ProfileSerializer
# from .forms import NeighLetterForm
from .models import Profile, Card

# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
  id = request.user.id
#   profile = Profile.objects.get(user=id)


  return render(request, 'index.html')


def card(request, id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  
  card = card.objects.get(pk=id)
  return render(request, 'card.html',{'profile':profile,'card':card})


def Newcard(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  current_user = request.user
  current_username = request.user.username

  if request.method == 'POST':
    form = NewcardForm(request.POST, request.FILES)
    if form.is_valid():
      card = form.save(commit=False)
      card.owner = current_user
      card.user = current_username
      card.card = profile.card
      card.save()
    return redirect('card')

  else:
    form = NewcardForm()

  return render(request, 'Newcard.html',{'form':form,'profile':profile})
