import os
import json
from django.http.response import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from backend.settings import BASE_DIR

from model.convert import convertImg

styles = ['Rajasthani', 'Mathali', 'Raja ravi verma', 'Gonsd']

class Convert(APIView):
    USER_IMG = os.path.join(BASE_DIR, 'static','user_img')


    def get(self, request):

        return Response(
            {'styles' : styles},
            status=status.HTTP_200_OK
            )

    def post(self, request):

        img = request.FILES.get('image')

        filename = Convert.USER_IMG + '\\' + img.name
        with open(filename, 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)

        convertImg(filename)

        return Response("ok")
