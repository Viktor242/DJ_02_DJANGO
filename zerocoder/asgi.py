#!/usr/bin/env python3
"""
ASGI config for zerocoder project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zerocoder.settings')

application = get_asgi_application()
