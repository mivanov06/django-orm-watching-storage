from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        non_closed_visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(),
            'is_strange': visit.is_long(),
        }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
