from rest_framework import serializers
from .models import ContactSubmission, QuoteRequest

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'

class QuoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model =