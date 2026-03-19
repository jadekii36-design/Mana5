def site_control(request):
    try:
        from accounts.models import SiteControl
        ctrl = SiteControl.objects.first()
    except Exception:
        ctrl = None
    return {'site_control': ctrl}
