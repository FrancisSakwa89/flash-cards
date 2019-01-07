from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
# from .forms import NeighForm, NewBusinessForm, ProfileForm,NewCommentForm, ContactForm, NewPostForm
# from .models import Neighbourhood, Business, Profile,NeighLetterRecipients,Post,Comment
# from .email import send_welcome_email
# from django.db.models import Avg
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializer import NeighbourhoodSerializer, ProfileSerializer
# from .forms import NeighLetterForm
# from .models import Profile, Post, Comment, Business, Neighbourhood, Contact

# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)


  return render(request, 'index.html',{'profile':profile})
