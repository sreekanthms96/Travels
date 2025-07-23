from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactSubmission, QuoteRequest, Review
from .serializers import ContactSubmissionSerializer, QuoteRequestSerializer, ReviewSerializer
from django.core.mail import send_mail
import requests
from django.conf import settings
from datetime import datetime
from rest_framework import generics

class ContactSubmissionView(APIView):
    def post(self, request):
        serializer = ContactSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            submission = serializer.save()
            subject = f'New Contact Submission from {submission.name} at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            send_mail(
                subject,
                f"Name: {submission.name}\nEmail: {submission.email}\nPhone: {submission.phone}\nMessage: {submission.message}",
                'sreekusree369@gmail.com',
                ['sreekanthsreenivas3@gmail.com'],
                fail_silently=False,
            )
            return Response({'message': 'We have received your request and will contact you soon.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuoteRequestView(APIView):
    def post(self, request):
        serializer = QuoteRequestSerializer(data=request.data)
        if serializer.is_valid():
            quote = serializer.save()
            subject = f'New Quote Request from {quote.name} at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            send_mail(
                subject,
                f"Name: {quote.name}\nEmail: {quote.email}\nPhone: {quote.phone}\nDestination: {quote.destination}\nMessage: {quote.message}",
                'sreekusree369@gmail.com',
                ['sreekanthsreenivas3@gmail.com'],
                fail_silently=False,
            )
            return Response({'message': 'We have received your request and will contact you soon.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer