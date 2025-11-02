from django.shortcuts import render

# Create your views here.
import asyncio
from django.http import JsonResponse, HttpRequest, HttpResponse
from typing import Dict, Any

# Asynchronous Support to handle I/O-bound tasks without blocking the main thread
async def async_http_view(request):
    """
    An asynchronous view that waits for a moment before responding
    This is useful for tasks that don't need immediate database access
    """
    await asyncio.sleep(2) # Simulate a non-blocking I/0 operation
    return JsonResponse({"message": "Hello from my async view!"})

# Type hinting for improved readability, error catches and easy maintainance
def get_user_data(request: HttpRequest) -> HttpResponse:
    """ Demonstrates the use of type hints for arguments and return values"""
    user_data: Dict[str, Any] = {
        'name': 'Egbuniwe Emmanuel',
        'role': ['Software Dev', 'Argicultural Economics']
    }
    return HttpResponse(f'User name: {user_data["name"]}')
