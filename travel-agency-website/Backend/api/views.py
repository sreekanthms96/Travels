from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactSubmission, QuoteRequest
from .serializers import ContactSubmissionSerializer, QuoteRequestSerializer
from django.core.mail import send_mail
import requests
from django.conf import settings

class ContactSubmissionView(APIView):
    def post(self, request):
        serializer = ContactSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            submission = serializer.save()
            send_mail(
                'New Contact Submission',
                f"Email: {submission.email}\nPhone: {submission.phone}\nMessage: {submission.message}",
                'test@example.com',
                ['your_email@example.com'],
                fail_silently=False,
            )
            return Response({'message': 'We have received your request and will contact you soon.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuoteRequestView(APIView):
    def post(self, request):
        serializer = QuoteRequestSerializer(data=request.data)
        if serializer.is_valid():
            quote = serializer.save()
            send_mail(
                'New Quote Request',
                f"Email: {quote.email}\nPhone: {quote.phone}\nDestination: {quote.destination}\nMessage: {quote.message}",
                'test@example.com',
                ['your_email@example.com'],
                fail_silently=False,
            )
            return Response({'message': 'We have received your request and will contact you soon.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)