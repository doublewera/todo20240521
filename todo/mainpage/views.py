from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    return render(
        request,
        'mainpage/index.html',
        {
            'kogda': datetime.now(), #.strftime('%Y %B %d')
            'tasks': [ # Они будут получены из базы данных, а не вбиты в код вручную!
                {
                    'description': 'Записать два видео по Django', 
                    'done': True,
                },
                {
                    'description': 'Провести урок', 
                    'done': True,
                },
                {
                    'description': 'Пробежать 5 километров', 
                    'done': False,
                },
            ],
        }
    )