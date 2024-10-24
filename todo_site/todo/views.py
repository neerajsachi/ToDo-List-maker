from django.shortcuts import render
from rest_framework.views import APIView
from .models import Todo
from rest_framework.response import Response
from .serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404

class ToDoList(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        todo=Todo.objects.all()
        serilaizer=ToDoSerializer(todo, many=True)
        return Response(serilaizer.data)
    
class ToDoGet(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            todo=Todo.objects.get(pk=pk)
            serializer=ToDoSerializer(todo)
            return Response(serializer.data)
        except Todo.DoesNotExist:
            return Response({'error': 'Todo not found'}, status=404)
        
class ToDoCreate(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ToDoUpdate(APIView):
    permission_classes=[IsAuthenticated]
    def put(self,request,pk):
        todo=Todo.objects.get(pk=pk)
        serializer=ToDoSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ToDoDelete(APIView):
    permission_classes=[IsAuthenticated]
    def delete(self,request,pk):
        todo=get_object_or_404(Todo,pk=pk)
        todo.delete()
        return Response({"Message": "Item deleted succesfully"},status=status.HTTP_200_OK)