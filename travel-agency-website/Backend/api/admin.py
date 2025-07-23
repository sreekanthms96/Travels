from django.contrib import admin
from .models import QuoteRequest, Destination, ContactSubmission

admin.site.register(QuoteRequest)
admin.site.register(Destination)
admin.site.register(ContactSubmission) 