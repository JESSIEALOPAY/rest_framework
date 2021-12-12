from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import News,Reporter
from news.api.serializers import NewsSerializer ,ReporterSerializer

# Class View
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class ReporterListCreateAPIView(APIView):
    def get(self,request):
        newsList= Reporter.objects.all()
        serializer= ReporterSerializer(newsList,many=True, context={'request': request})
        return Response(serializer.data)

    def post(self,request):
        serializer= ReporterSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)



class NewsListCreateAPIView(APIView):
    def get(self,request):
        newsList= News.objects.filter(active=True)
        serializer= NewsSerializer(newsList,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer= NewsSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)



class NewsDetailAPIView(APIView):
    def get_object(self,id):
        newsInstance= get_object_or_404(News,id=id)
        return newsInstance
    
    def get(self,request,id):
        newInstance= self.get_object(id)
        serializer= NewsSerializer(newInstance)
        return Response(serializer.data)

    def put(self,request,id):
        newsInstance= self.get_object(id)
        serializer= NewsSerializer(newsInstance,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        news= self.get_object(id)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









# #Functions Based Views
# @api_view(["GET","POST"])
# def news_list_create_api_view(request):
#     if request.method=="GET":
#         newsList = News.objects.filter(active= True)
#         serializer= NewsSerializer(newsList,many=True)
#         return Response(serializer.data)

#     elif request.method=="POST":
#         serializer= NewsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
        

# @api_view(["GET","PUT","DELETE"])
# def news_detail_api_view(request,id):
#     try:
#         news_instance= News.objects.get(id=id)
#     except News.DoesNotExist:
#         return Response({
#             "errors":{
#                 "code":400,
#                 "message":f"bu id:{id} ile haber bulunamadı"
#             }
#         },status=status.HTTP_400_BAD_REQUEST)
#     if request.method=="GET":
#         serializer= NewsSerializer(news_instance)
#         return Response(serializer.data)     

#     elif request.method=="PUT":
#         serializer= NewsSerializer(news_instance,request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response({
#             "errors":{
#                 "code":400,
#                 "message":f"girdiğiniz bilgileri lütfen tekrar kontrol ediniz"
#             }})

#     elif request.method=="DELETE":
#         news_instance.delete()
#         return Response({
#             "Response":{
#                 "success":True,
#                 "messages":"News has been deleted succefully"
#             }
#         },status=status.HTTP_204_NO_CONTENT)




