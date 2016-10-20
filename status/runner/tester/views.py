# BuiltIn django and rest_framework packages
from django.shortcuts import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.core.exceptions import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
import urllib.parse
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.db import connection
import binascii
import os
from django.conf import settings
from django.utils.timezone import now
from django.db import connection

class Userss(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        if request.user.is_authenticated():
            return Response({"info": "user authenticated"}, status=status.HTTP_200_OK)
        else:
            return Response({"info": " user is not authenticated"}, status=status.HTTP_409_CONFLICT)

    def post(self, request, format=None):
        if not request.user.is_authenticated():
            email = request.data['email']
            isactive = 1
            user = User.objects.create_user(username =  email, email = email, is_active = isactive, password = 'qwerty')
            user.save()
            return Response({"info": "Sucessfully Registered"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"info": "user authenticated"}, status=status.HTTP_409_CONFLICT)

class UserLog(APIView):

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        if request.user.is_authenticated():
            logout(request)
            return Response({"info": "user logged out"}, status=status.HTTP_200_OK)
        else:
            return Response({"info": "user is not authenticated"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if not request.user.is_authenticated():
            email = request.data['email']
            password = request.data['password']
            u = User.objects.get(email = email)
            user = authenticate(username = u.username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['member_id'] = email
                    return Response({"info": "sucessfully logged in"}, status=status.HTTP_200_OK)
                else:
                    return Response({"info": "user dosent exists"}, status=status.HTTP_409_CONFLICT)
            else:
                return Response({"info": "user dosent exists"}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"info": "user authenticated"}, status=status.HTTP_200_OK)
