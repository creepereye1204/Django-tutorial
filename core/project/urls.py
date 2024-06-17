import logging

from django.contrib import admin
from django.urls import path

logger = logging.getLogger('tuna')
logger.debug('This is debug message')
logger.info('This is info message')

urlpatterns = [
    path('admin/', admin.site.urls),
]
