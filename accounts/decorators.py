from django.shortcuts import redirect


def admin_required(
    function=None,
    redirect_to="/",
):
    """
    Decorator for views that checks that the logged-in user is a superuser,
    redirects to the specified URL if necessary.
    """

    # Define the test function: checks if the user is active and a superuser
    def test_func(user):
        return user.is_active and user.is_superuser

    # Define the wrapper function to handle the response
    def wrapper(request, *args, **kwargs):
        if test_func(request.user):
            # Call the original function if the user passes the test
            return function(request, *args, **kwargs) if function else None
        # Redirect to the specified URL if the user fails the test
        return redirect(redirect_to)

    return wrapper if function else test_func


def lecturer_required(
    function=None,
    redirect_to="/",
):
    """
    Decorator for views that checks that the logged-in user is a superuser,
    redirects to the specified URL if necessary.
    """

    # Define the test function: checks if the user is active and a superuser
    def test_func(user):
        return user.is_active and user.is_lecturer or user.is_superuser

    # Define the wrapper function to handle the response
    def wrapper(request, *args, **kwargs):
        if test_func(request.user):
            # Call the original function if the user passes the test
            return function(request, *args, **kwargs) if function else None
        # Redirect to the specified URL if the user fails the test
        return redirect(redirect_to)

    return wrapper if function else test_func


def student_required(
    function=None,
    redirect_to="/",
):
    """
    Decorator for views that checks that the logged-in user is a superuser,
    redirects to the specified URL if necessary.
    """

    # Define the test function: checks if the user is active and a superuser
    def test_func(user):
        return user.is_active and user.is_student or user.is_superuser

    # Define the wrapper function to handle the response
    def wrapper(request, *args, **kwargs):
        if test_func(request.user):
            # Call the original function if the user passes the test
            return function(request, *args, **kwargs) if function else None
        # Redirect to the specified URL if the user fails the test
        return redirect(redirect_to)

    return wrapper if function else test_func


# ########################################################
# Rate Limiting Decorator (Brute-Force Protection)
# ########################################################

from functools import wraps
from django.core.cache import cache
from django.http import HttpResponseForbidden


def rate_limit_ip(limit=5, window=60):
    """
    Decorator to limit the number of requests from a single IP address.
    
    Args:
        limit (int): Maximum number of requests allowed within the window.
        window (int): Time window in seconds.
    
    Returns:
        Decorated function that enforces rate limiting.
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Get the client's IP address
            ip_address = get_client_ip(request)
            cache_key = f"rate_limit_{ip_address}_{view_func.__name__}"
            
            # Get current attempt count
            attempts = cache.get(cache_key, 0)
            
            if attempts >= limit:
                return HttpResponseForbidden(
                    "Too many login attempts. Please try again later."
                )
            
            # Increment attempt count
            cache.set(cache_key, attempts + 1, window)
            
            return view_func(request, *args, **kwargs)
        
        return wrapper
    return decorator


def get_client_ip(request):
    """Extract the client's IP address from the request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
