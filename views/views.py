from django.http import JsonResponse
from django.template.loader import render_to_string


def sales_by_countries(request):
    data = [
        {
            'country': 'United States',
            'flag_url': 'media/flags/united-states.svg',
            'description': 'Direct link clicks',
            'visits': '9,763',
            'change': '2.6%',
            'change_type': 'up'
        },
        {
            'country': 'Brazil',
            'flag_url': 'media/flags/brazil.svg',
            'description': 'All Social Channels',
            'visits': '4,062',
            'change': '0.4%',
            'change_type': 'down'
        }
  
    ]
    html = render_to_string('_widget_sale_by_countries.html', {'items': data})
    return JsonResponse({'html': html})
