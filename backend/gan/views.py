import os
import json
import random
import string
from django.http.response import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from backend.settings import BASE_DIR

from model.convert import convertImg

styles = ['Rajasthani', 'Mathali', 'Raja ravi verma', 'Gond']


def gen():
    return string.ascii_letters + string.digits

def id():
    return ''.join([random.choice(gen()) for _ in range(0,10)])

class Convert(APIView):
    USER_IMG = os.path.join(BASE_DIR, 'static','user_img')


    def get(self, request):

        return Response(
            {'styles' : styles},
            status=status.HTTP_200_OK
            )

    def post(self, request):
        img = request.FILES.get('image')
        style = request.POST.get('style')

        imgName = id() + '.' + img.content_type.split('/')[1]

        # Path to store user upload images
        userImg = os.path.join(Convert.USER_IMG, imgName)

        with open(userImg, 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)

        result = convertImg(userImg, style)

        return Response({
            "result" : result
        }, status=status.HTTP_200_OK)
