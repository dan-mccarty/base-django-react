# django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import redirect

# drf
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# general
from pprint import pprint as pp


User = get_user_model()



# ... custom views ...