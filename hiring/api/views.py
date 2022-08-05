from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView, 
    CreateAPIView,
)
from hiring.models import Hiring
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import HiringViewSerializer, HiringSerializer
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwnerPermission, isSuperAdminUser

class PaginationApi(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class HiringApiView(ListAPIView):
    queryset = Hiring.objects.all()
    serializer_class = HiringViewSerializer
    permission_classes = (AllowAny,)
    pagination_class  = PaginationApi


class HiringDetailApiView(RetrieveAPIView):
    queryset = Hiring.objects.all()
    serializer_class = HiringViewSerializer
    permission_classes = (AllowAny,)


class HiringCreateApiView(CreateAPIView):
    queryset = Hiring.objects.all()
    serializer_class = HiringSerializer
    permission_classes = (IsAuthenticated, isSuperAdminUser)


class HiringDeleteApiView(RetrieveUpdateAPIView):
    queryset = Hiring.objects.all()
    serializer_class = HiringSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission, isSuperAdminUser)


class HiringUpdateApiView(RetrieveDestroyAPIView):
    queryset = Hiring.objects.all()
    serializer_class = HiringSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission, isSuperAdminUser)