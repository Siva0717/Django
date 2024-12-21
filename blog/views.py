from typing import Self
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Room, hotel, shop, university,inventory
from . forms import StudentForm, schoolForm, hotelForm, shopForm
from .serializer import hotelSerializer, universitySerializer,inventorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


def room(request, pk):
    room=Room.object.get(id=pk)
    return render(request, 'room.html')

def home(request):
    rooms=Room.objects.all()
    return render(request, 'home.html',  {'rooms':rooms})

def main(request):
    return render(request, 'main.html')

def create(request):

    form=StudentForm()
    if request.method =='POST':
        form =StudentForm(request.POST)
        if form.is_valid():
            form.save()
    context ={'form':form}
    return render(request, 'create.html', context)



def dep(request):  
    form=schoolForm()
    if request.method=='POST':
        form=schoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/final')
    return render(request, 'school.html', {'form':form})
def final(request):
    return HttpResponse('<h1><b> Form submitted successfully</h1></b>')


def final(request):
    form=shopForm()
    if request.method=='POST':
        form=shopForm(request.POST)
        form.save()
    return render(request, 'update.html', {'form':form})

def office(request):
    form=hotelForm()
    form=hotel.objects.all()
    
    
    return render(request, 'office.html', {'form':form})


        
@api_view(['GET'])
def getSiva(request):
    obj=hotel.objects.all()
    serializer=hotelSerializer(obj, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def post(request):
   serializer=hotelSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=200)
   else:
       return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete(request, id):
       obj=hotel.objects.get(id=id)
       obj.delete()
       return Response({"message":"successfully deleted"})
@api_view(['patch'])
def patch(request, id):
    obj=hotel.objects.get(id=id)
    data=request.data
    serializer=hotelSerializer(obj, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    else:
        return Response(serializer.errors, status=400)
    
@api_view(['put'])
def put(request, id):
    obj=hotel.objects.get(id=id)
    data=request.data
    serializer=hotelSerializer(obj, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    else:
        return Response(serializer.errors, status=400)
@api_view(['POST', 'GET'])
def api1(request):
    if request.method=='POST':
        data=request.data
        serializer=universitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    else:
        obj=university.objects.all()
        serializer=universitySerializer(obj, many=True)
        return Response(serializer.data, status=200)
@api_view(['DELETE'])
def api2(request, id):
    boj=university.objects.get(id=id)
    boj.delete()
    return Response(university.data, status=200)
@api_view(['GET'])
def api3(request, name):
    obj=university.objects.filter(name=name)
    final=list(obj.values())
    return Response(final, status=200)
@api_view(['GET'])
def api4(request):
    obj=university.objects.all().order_by('seats')
    final=list(obj.values())
    return Response(final, status=200)
@api_view(['PATCH'])
def api5(request, id):
    bj=university.objects.get(id=id)
    data=request.data
    serilizer=universitySerializer(bj,data=data, partial=True)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data, status=200)
    else:
        return Response(serilizer.errors, status=400)
    
@api_view(['PUT','PATCH','POST'])
def api7(request,id):
    
        obj=inventory.objects.get(id=id)
        data=request.data
        serializer=inventorySerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
        

            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
@api_view(['POST'])  
def api6(request):  
         data=request.data
         serializer=inventorySerializer(data=data)
         if serializer.is_valid():
                serializer.save()
        

                return Response(serializer.data, status=200)
         else:
             return Response(serializer.errors, status=400)
       
@api_view(['PUT','PATCH','POST'])
def api8(request,id):
    
        obj=inventory.objects.get(id=id)
        data=request.data
        serializer=inventorySerializer(obj, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
        

            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

        

        










