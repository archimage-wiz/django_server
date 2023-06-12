from django.shortcuts import render

from demo_page.models import Logg


# Create your views here.

def demo_page(request):

    visitor_addr = request.META.get('REMOTE_ADDR', 'unknown')
    if log_obj := Logg.objects.filter(ip_addr=visitor_addr):
        log_obj = log_obj[0]
        log_obj.visits += 1
    else:
        log_obj = Logg(ip_addr=visitor_addr)

    context = {
        'ipaddr': log_obj.ip_addr,
        'lastvisit': log_obj.last_visit,
        'counter': log_obj.visits
    }

    log_obj.save()

    return render(request, 'index.html', context)
