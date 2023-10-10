from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .models import SchairData,Advice

def schair_data_api(request):
    status = request.GET.get('status', 0)
    
    if status == '1':
        activity = "A person is bending to the left side of a chair"
        advice_text = "It's not good for your health to sit in this way. Try to maintain a balanced posture."
    elif status == '2':
        activity = "A person is bending to the right side of a chair"
        advice_text = "It's not good for your health to sit in this way. Try to maintain a balanced posture."
    elif status == '3':
        activity = "A person is seated wrongly in the central position of a chair"
        advice_text = "It's not good for your health to sit in this way. Try to maintain a balanced posture."
    else:
        activity = "Normal"
        advice_text = "Good job! Your health is in good condition. Keep up the good posture."

    schair_data = SchairData.objects.create(datetime=datetime.now(), activity=activity)
    advice = Advice.objects.create(activity=schair_data, advice_text=advice_text)

    return JsonResponse({'message': 'Data received successfully', 'context': {'activity': activity, 'advice': advice_text}})


def schair_data_view(request):
    latest_entry = SchairData.objects.latest('datetime')
    advice = Advice.objects.get(activity=latest_entry)

    activity = latest_entry.activity
    advice_text = advice.advice_text

    return render(request, 'schair_app/schair_data_view.html', {'activity': activity, 'advice': advice_text})

