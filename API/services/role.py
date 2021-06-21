from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from API.model.role import Role
from API.serializers.role import RoleSerializer
from Common.exception import Unauthorized


class RoleAPI(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            role = Role.objects.get(id=request.query_params.get('id'))
            serializer = RoleSerializer(role)
            result = serializer.data
            return Response(result, status=status.HTTP_200_OK)
        except Unauthorized:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as exc:
            return Response(exc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            # checkUser(request, UserType.ADMINISTRADOR.value)
            serializer = RoleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Unauthorized:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as exc:
            return Response(exc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *arg, **kwargs):
        try:
            # checkUser(request, UserType.ADMINISTRADOR.value)
            serializer = RoleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.update()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Unauthorized:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as exc:
            return Response(exc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RoleListAPI(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            # checkUser(request, UserType.ADMINISTRADOR.value)
            result = []
            roles = list(Role.objects.filter(
                name__unaccent__icontains=request.query_params.get("name"),
                description__unaccent__icontains=request.query_params.get("description")))
            for role in roles:
                serializer = RoleSerializer(role)
                result.append(serializer.data)
            return Response(result, status=status.HTTP_200_OK)
        except Unauthorized:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as exc:
            return Response(exc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
