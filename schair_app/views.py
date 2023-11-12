from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .models import SchairData, Advice
from django.contrib.auth.decorators import login_required

def schair_data_api(request):
    # Assuming 'status' is passed in the request
    status = request.GET.get('status', None)

    if status is not None:
        if status == '1':
            activity = "Abnormal"
            advice_text = "A person is bending to the left side of a chair"
        elif status == '2':
            activity = "Abnormal"
            advice_text = "A person is bending to the right side of a chair"
        elif status == '3':
            activity = "Abnormal"
            advice_text = "A person is seated wrongly in the central position of a chair."
        elif status == '0':
            activity = "Normal"
            advice_text = "A person is seated in the good posture."

        else:
            activity = ""
            advice_text = ""

        schair_data = SchairData.objects.create(datetime=datetime.now(), activity=activity)
        advice = Advice.objects.create(activity=schair_data, advice_text=advice_text)

        return JsonResponse({'message': 'Data received successfully', 'context': {'activity': activity, 'advice': advice_text}})
    else:
        return JsonResponse({'error': 'Invalid request. Status parameter is missing.'}, status=400)


@login_required
def schair_data_view(request):
    latest_entry = SchairData.objects.latest('datetime')
    advice = Advice.objects.get(activity=latest_entry)

    activity = latest_entry.activity
    advice_text = advice.advice_text

    return render(request, 'schair_app/schair_data_view.html', {'activity': activity, 'advice': advice_text})



def update_data(request):
    latest_entry = SchairData.objects.latest('datetime')
    advice = Advice.objects.get(activity=latest_entry)

    activity = latest_entry.activity
    advice_text = advice.advice_text

    return JsonResponse({'activity': activity, 'advice': advice_text})

# dashboard
from django.db.models import Count
from django.shortcuts import render
from .models import SchairData, Advice

def dashboard_data(request):
    schair_data_with_advice = SchairData.objects.select_related('advice').all()

    # Calculate the count of normal and abnormal activities
    normal_count = SchairData.objects.filter(activity='Normal').count()
    abnormal_count = SchairData.objects.exclude(activity='Normal').count()

    context = {
        'schair_data_with_advice': schair_data_with_advice,
        'normal_count': normal_count,
        'abnormal_count': abnormal_count,
    }
    return render(request, 'schair_app/chart_data_view.html', context)
