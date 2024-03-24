from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.exceptions import AuthenticationFailed
from . serializers import UserSerializer
from . models import User
import logging


# Create your views here.

logger = logging.getLogger("__name__")

class Register(APIView):
    def post(self, request):
        seralizer = UserSerializer(data=request.data)
        seralizer.is_valid(raise_exception=True)
        seralizer.save()
        return Response(seralizer.data)
    
class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            logger.exception("User Not Found !")
            raise AuthenticationFailed('User Not Found !')

        if user.check_password(password):
            logger.exception("Password didn't matched !")
            raise AuthenticationFailed("Password didn't matched !")
        
        # payload = {
        #     'id': user.id,
        #     'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=60),
        #     'iat': datetime.datetime.now(datetime.timezone.utc)
        # }

        # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        # respose = Response()
        # respose.set_cookie(key='jwt', value=token, httponly=True)
        # respose.data = {
        #     'jwt':token
        # }

        return Response({
            "message": "Login Successfully"
        })