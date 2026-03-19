"""
SiteExpiryMiddleware
- Grace period (0–3 days past expiry): clients can still use the site,
  but see a polite reminder overlay (handled in base.html via context_processor).
- Fully blocked (>3 days past expiry): redirect all client pages to /service-unavailable/.
"""

from django.shortcuts import redirect
from django.urls import reverse

# URLs that are always accessible (never blocked)
_ALWAYS_ALLOWED = (
    '/admin/',
    '/staff/',
    '/service-unavailable/',
    '/static/',
    '/media/',
)


class SiteExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # Skip always-allowed paths
        if any(path.startswith(p) for p in _ALWAYS_ALLOWED):
            return self.get_response(request)

        # Check SiteControl
        try:
            from accounts.models import SiteControl
            ctrl = SiteControl.objects.first()
            if ctrl and ctrl.is_fully_blocked:
                return redirect('/service-unavailable/')
        except Exception:
            pass  # If DB not ready, allow access

        return self.get_response(request)
