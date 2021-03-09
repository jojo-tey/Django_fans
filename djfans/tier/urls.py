from django.urls import path
from tier.views import NewTier

urlpatterns = [
    path('newtier/', NewTier, name='newtier'),
]
