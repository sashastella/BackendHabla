from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from API.model.profile import Profile
from API.serializers.profile import ProfileSerializer
from API.serializers.user import UserSerializer
from API.serializers.userSimple import UserSimpleSerializer
from Common.enums import RequestType
from Common.exception import Unauthorized


class UserAPI(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            # checkUser(request, UserType.ADMINISTRADOR.value)
            user = Profile.objects.get(user_id=request.query_params.get("id"))
            profile = ProfileSerializer(user)
            profile.set_user(user.user)
            result = profile.data
            return Response(result, status=status.HTTP_200_OK)
        except Unauthorized:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as exc:
            return Response(exc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            # checkUser(request, UserType.ADMINISTRADOR.value)
            user_serializer = UserSerializer(data=request.data)
            profile_serializer = ProfileSerializer(data=request.data)
            user_serializer.set_requestType(RequestType.POST)
            if user_serializer.is_valid() and profile_serializer.is_valid():
                user = user_serializer.save()
                profile_serializer.set_user(user)
                profile_serializer.save()
                return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
            else:
                if not user_serializer.is_valid():
                    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Unauthorized:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as exc:
            return Response(exc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *arg, **kwargs):
        try:
            # checkUser(request, UserType.ADMINISTRADOR.value)
            user_serializer = UserSimpleSerializer(data=request.data)
            user_serializer.set_requestType(RequestType.PUT)
            profile_serializer = ProfileSerializer(data=request.data)
            if user_serializer.is_valid() and profile_serializer.is_valid():
                user = user_serializer.update()
                profile_serializer.set_user(user)
                profile_serializer.update()
                return Response(None, status=status.HTTP_200_OK)
            else:
                if not user_serializer.is_valid():
                    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Unauthorized:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as exc:
            return Response(exc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserList(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        # checkUser(request, UserType.ADMINISTRADOR.value)
        try:
            result = []
            profiles = list(Profile.objects.filter(
                user__first_name__unaccent__icontains=request.query_params.get("first_name"),
                user__last_name__unaccent__icontains=request.query_params.get("last_name"),
                user__email__icontains=request.query_params.get("email")))
            for profile in profiles:
                serializer = ProfileSerializer(profile)
                serializer.set_user(profile.user)
                result.append(serializer.data)
            return Response(result, status=status.HTTP_200_OK)
        except Unauthorized:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as exc:
            return Response(exc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)