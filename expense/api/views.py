from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Expense
from .serializer import ExpenseSerializer

# Create your views here.
@api_view(['GET'])
def get_Expense(req):
    expense = Expense.objects.all()
    serializer = ExpenseSerializer(expense,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_expense(req):
    serializer = ExpenseSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def expense_detail(req,pk):
    expense = get_object_or_404(Expense,pk=pk)
    if req.method == 'GET':
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)
    
    if req.method == 'PUT':
        serializer = ExpenseSerializer(expense,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if req.method == 'DELETE':
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        