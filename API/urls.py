from django.urls import path

from API.services.role import RoleAPI, RoleListAPI
from API.services.user import UserList, UserAPI
from API.services.victim import VictimListAPI, VictimAPI

urlpatterns = [
    path('userList/', UserList.as_view(), name='userList'),
    path('user/', UserAPI.as_view(), name='user'),
    path('role/', RoleAPI.as_view(), name='rol'),
    path('roleList/', RoleListAPI.as_view(), name='roleList'),
    path('victim/', VictimAPI.as_view(), name='victim'),
    path('victimList/', VictimListAPI.as_view(), name='victimList'),

]