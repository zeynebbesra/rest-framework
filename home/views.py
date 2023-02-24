from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from home.models import Person
from home.serializers import PersonSerializer, LoginSerializer, RegisterSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



class RegisterAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status' : False,
                'message' : serializer.errors
            } , status.HTTP_400_BAD_REQUEST)
        
        serializer.save()

        return Response({'status' : True, 'message': 'user created'},  status.HTTP_201_CREATED)


class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                'status' : False,
                'message' : serializer.errors
            } , status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username = serializer.data['username'], password = serializer.data['password'])
        if not user:
            return Response({
                'status' : False,
                'message' : 'invalid credentials'
            } , status.HTTP_400_BAD_REQUEST)
        
        token, _ = Token.objects.get_or_create(user = user)

        return Response({'status' : True, 'message': 'user login', 'token' : str(token)},  status.HTTP_200_OK)

 
class PersonAPI(APIView):

    def get(self, request):
        objs = Person.objects.all()
        serializer = PersonSerializer(objs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request):
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})



# @api_view(['POST']) 
# def login(request):
#     data = request.data
#     serializer = LoginSerializer(data = data)
#     if serializer.is_valid():
#         data = serializer.data
#         return Response({'message': 'succes'})
#     return Response(serializer.errors)



# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def person(request):
#     if request.method == "GET":
#         objs = Person.objects.all()
#         serializer = PersonSerializer(objs, many=True)
#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         data = request.data
#         serializer = PersonSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors)

#     elif request.method == 'PUT':
#         data = request.data
#         serializer = PersonSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors)
    
#     elif request.method == 'PATCH':
#         data = request.data
#         obj = Person.objects.get(id = data['id'])
#         serializer = PersonSerializer(obj, data = data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors)
    
#     else:
#         data = request.data
#         obj = Person.objects.get(id = data['id'])
#         obj.delete()
#         return Response({'message': 'person deleted'})
