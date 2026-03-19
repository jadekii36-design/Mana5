def site_control(request):
    # Skip for Django admin — avoids interfering with admin pages
    if request.path.startswith('/admin/'):
        return {}
    try:
        from accounts.models import SiteControl
        ctrl = SiteControl.objects.first()
    except Exception:
        ctrl = None
    return {'site_control': ctrl}
