from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Inventory
from .serializers import InventorySerializer

class InventoryList(APIView):
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def get(self, request):
        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data, content_type='application/json')
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        renderer_context = renderer_context or {}
        renderer_context['response'].accepted_media_type = 'application/json'
        return super().render(data, accepted_media_type, renderer_context)

class InventoryDetail(APIView):
    def delete(self, request, pk):
        inventory = self.get_object(pk)
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, content_type='application/json')

    def put(self, request, pk):
        inventory = self.get_object(pk)
        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def get_object(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, content_type='application/json')

class InventoryCategory(APIView):
    def get(self, request, category):
        items = Inventory.objects.filter(category=category)
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data, content_type='application/json')

class InventorySort(APIView):
    def get(self, request):
        items = Inventory.objects.order_by('-price')
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data, content_type='application/json')


#-----------------------------------------------------------------------------------
# Another code
# from rest_framework import status
# from django.http import JsonResponse
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Inventory
# from .serializers import InventorySerializer

# class InventoryList(APIView):
#     def post(self, request):
#         serializer = InventorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request):
#         items = Inventory.objects.all()
#         serializer = InventorySerializer(items, many=True)
#         return Response(serializer.data)

# class InventoryDetail(APIView):
#     def delete(self, request, pk):
#         try:
#             inventory = Inventory.objects.get(pk=pk)
#             inventory.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Inventory.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, pk):
#         try:
#             inventory = Inventory.objects.get(pk=pk)
#             serializer = InventorySerializer(inventory, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Inventory.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

# class InventoryCategory(APIView):
#     def get(self, request, category):
#         items = Inventory.objects.filter(category=category)
#         serializer = InventorySerializer(items, many=True)
#         return Response(serializer.data)

# class InventorySort(APIView):
#     def get(self, request):
#         items = Inventory.objects.order_by('-price')
#         serializer = InventorySerializer(items, many=True)
#         return Response(serializer.data)
