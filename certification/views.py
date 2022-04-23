from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from certification.models import certification
from certification.serializer import certificationSerializer


@api_view(['GET', 'POST', 'DELETE'])
def certification_list(request):
   if request.method == 'GET':
        tutorials = certification.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            certification = certification.filter(title__icontains=title)
        
        certification_serializer = certificationSerializer(certification, many=True)
        return JsonResponse(certification_serializer.data, safe=False)
        # 'safe=False' for objects serialization
   elif request.method == 'POST':
        certification_data = JSONParser().parse(request)
        certification_serializer = certificationSerializer(data=certification_data)
        if certification_serializer.is_valid():
            certification_serializer.save()
            return JsonResponse(certification_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(certification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET', 'PUT', 'DELETE'])
def certification_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        certification = certification.objects.get(pk=pk) 
    except certification.DoesNotExist: 
        return JsonResponse({'message': 'The certification does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET': 
        certification_serializer = certificationSerializer(certification) 
        return JsonResponse(certification_serializer.data) 
    elif request.method == 'PUT': 
        certification_data = JSONParser().parse(request) 
        certification_serializer = certificationSerializer(certification, data=certification_data) 
        if certification_serializer.is_valid(): 
            certification_serializer.save() 
            return JsonResponse(certification_serializer.data) 
        return JsonResponse(certification_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
        
