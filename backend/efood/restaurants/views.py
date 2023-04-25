from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Restaurant
from .serializers import RestaurantSerializer, RestaurantCreateSerializer, RestaurantDetailSerializer


class RestaurantView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantDetailSerializer

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Restaurant.objects.filter(id=self.kwargs['pk'])

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        email = serializer.validated_data.get('email')
        if email:
            subject = 'Restaurant'
            message = 'Thank you for staying with us'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject,
                      message,
                      from_email,
                      recipient_list,
                      fail_silently=False,
                      )

        return Response(serializer.data)


class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer
    permission_classes = (permissions.IsAdminUser,)
