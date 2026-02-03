from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Application, Job

from .serializers import ApplicationSerializer, JobsSerializer, RegisterSerializer
@api_view(['GET'])
def hello_api(request):
    return Response({"message":"hello from django API"})

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"User Registered SucessFully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def basic_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"user_id": user.id, "username": user.username, "token": token.key, "message":"Login Sucessfull"}, status=status.HTTP_200_OK)
    else:
        return Response({"message":"Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def job_list(request):
    jobs = Job.objects.all()
    serializer = JobsSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_job(request):
    # Job ID still comes from the Data
    job_id = request.data.get('job')
    
    # Applicant comes from the Token (Secure)
    applicant = request.user
    
    # check application exists
    if Application.objects.filter(job=job_id, applicant=applicant).exists():
        return Response({"message":"You have already applied for this job"}, status=status.HTTP_400_BAD_REQUEST)
        
    serializer = ApplicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(applicant=applicant)
        return Response({"message":"Application Submitted Successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)