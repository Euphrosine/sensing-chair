from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .models import SchairData

def schair_data_api(request):
    status = request.GET.get('status', 0)
    
    if status == '1':
        activity = "A person is bending to the left side of a chair"
        advice = "It's not good for your health to sit in this way. Try to maintain a balanced posture."
    elif status == '2':
        activity = "A person is bending to the right side of a chair"
        advice = "It's not good for your health to sit in this way. Try to maintain a balanced posture."
    elif status == '3':
        activity = "A person is seated wrongly in the central position of a chair"
        advice = "It's not good for your health to sit in this way. Try to maintain a balanced posture."
    else:
        activity = "Normal"
        advice = "Good job! Your health is in good condition. Keep up the good posture."

    SchairData.objects.create(datetime=datetime.now(), activity=activity)

    return JsonResponse({'message': 'Data received successfully', 'context': {'activity': activity, 'advice': advice}})


def schair_data_view(request):
    schair_data = SchairData.objects.all()
    return render(request, 'schair_app/schair_data_view.html', {'schair_data': schair_data})
