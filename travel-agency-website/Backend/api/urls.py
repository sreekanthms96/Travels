from django.urls import path
from .views import ContactSubmissionView, QuoteRequestView, ReviewListCreateView

urlpatterns = [
    path('contact/', ContactSubmissionView.as_view(), name='contact_submission'),
    path('quote/', QuoteRequestView.as_view(), name='quote_request'),
    path('reviews/', ReviewListCreateView.as_view(), name='review_list_create'),
]