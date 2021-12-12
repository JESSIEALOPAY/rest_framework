from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile , ProfileStatus
from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer ,ProfileImageSerializer
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet , ModelViewSet
from rest_framework import mixins
from profiles.api.permissions import ProfileOwnerOrReadOnly ,ProfileStatusOwnerOrReadOnly
from rest_framework.filters import SearchFilter

# from django.contrib.auth.models import User
# from django.db.models.query import QuerySet
# from pprint import pprint
# from rest_framework.response import Response

class ProfileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ProfileOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['user__username', 'bio']




    # def list(self, request, *args, **kwargs):
    #         queryset = self.filter_queryset(self.get_queryset())
    #         # pprint(self.request.query_params)
    #         # queryDict=dict(request.GET)
    #         # pprint(queryDict)
    #         page = self.paginate_queryset(queryset)
    #         if page is not None:
    #             serializer = self.get_serializer(page, many=True)
    #             return self.get_paginated_response(serializer.data)

    #         serializer = self.get_serializer(queryset, many=True)
    #         return Response(serializer.data)




class ProfieStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated,ProfileStatusOwnerOrReadOnly]

    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username=self.request.query_params.get("username",None)
        if username:
            queryset=queryset.filter(user_profile__user__username__contains=username)
        return queryset

    def perform_create(self, serializer):
        user_profile= self.request.user.profile
        return serializer.save(user_profile=user_profile)



class ProfileImageUpdateView(generics.UpdateAPIView):

    serializer_class= ProfileImageSerializer
    permission_classes= [IsAuthenticated]
    def get_object(self):
        user_profile= self.request.user.profile 
        return user_profile




# class ProfileViewSet(ReadOnlyModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = (IsAuthenticated,)





# class ProfilesList(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = (IsAuthenticated,)

