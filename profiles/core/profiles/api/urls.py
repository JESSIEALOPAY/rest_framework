from django.urls import path ,include
from profiles.api.views import ProfileViewSet,ProfieStatusViewSet,ProfileImageUpdateView
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r"profiles",ProfileViewSet)
router.register(r"status", ProfieStatusViewSet,basename="status")

urlpatterns=[
    path("",include(router.urls)),
    path("profile_image/",ProfileImageUpdateView.as_view(),name="profile-image"),
]





# profile_list= ProfileViewSet.as_view({"get":"list"})
# profile_detail= ProfileViewSet.as_view({"get":"retrieve"})

# urlpatterns = [
#     path("profile-list/", profile_list, name="profiles"),
#     path("profile-list/<int:pk>", profile_detail, name="profiles"),
# ]


# from profiles.api import views
# urlpatterns = [
#     path("profile-list/", views.ProfilesList.as_view(), name="profiles"),
# ]