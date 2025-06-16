from rest_framework.views import APIView, Response
from .serializers import UserSerializerNew, UserSerializerLogin
from .models import User

# Create your views here.

class Cadastro(APIView):
    def post(self, request):
        user = UserSerializerNew(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=201)
        return Response(user.errors, status=400)
    
class Login(APIView):
    def post(self, request):
        serializer_data = UserSerializerLogin(data=request.data)

        if serializer_data.is_valid():
            user = serializer_data.validated_data['user']

            return Response({'email':user.email, 'nome':user.nome}, status=200)
        return Response(serializer_data.errors, status=400)