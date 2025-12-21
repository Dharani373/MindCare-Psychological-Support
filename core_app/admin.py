from django.contrib import admin
from .models import StressQuestion, StressResponse

admin.site.register(StressQuestion)
admin.site.register(StressResponse)
