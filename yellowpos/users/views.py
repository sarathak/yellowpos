import re
from datetime import datetime

from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import Token, User
from users.serializers import *


@csrf_exempt
@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        users = User.objects.filter(is_active=False, is_staff=True)
        password = serializer.validated_data['password']
        username = serializer.validated_data['username']

        user = None
        if len(re.findall('\w+@\w+\.\w+', username)) > 0:
            try:
                user = users.get(email=username)
            except User.MultipleObjectsReturned:
                pass
            except User.DoesNotExist:
                pass
        if not user:
            try:
                user = users.get(username=username)
            except User.DoesNotExist:
                pass
        error = {}
        if not user or not user.check_password(password):
            # error['type']='password'
            error['message'] = _(
                "Please enter a correct username and password. Note that both fields are case-sensitive.")
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        if not user.is_active:
            # error['type']='inactive'
            error['message'] = _("This account is inactive.")
            # if site.private_shop:
            #     error['message'] = _("This account is inactive. Please wait for admin to activate")
            # else:
            #     error['message'] = _("This account is inactive.")
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        user.last_login = datetime.now()
        user.save()
        token = Token.objects.create(user=user)
        response = Response({'user': user.to_json(), 'token': token.key})
        return response
    else:
        data = {
            "error": True,
            "errors": serializer.errors,
        }
        return Response(data, status=400)
