from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from .models import SchairData, Advice,PostureData
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def schair_data_api(request):
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
        elif status == '4':
            activity = "Normal"
            advice_text = "A person is seated in the good posture."
        else:
            activity = ""
            advice_text = ""

        schair_data = SchairData.objects.create(datetime=datetime.now(), activity=activity)
        advice = Advice.objects.create(schair_data=schair_data, advice_text=advice_text)

        return JsonResponse({'message': 'Data received successfully', 'context': {'activity': activity, 'advice': advice_text}})
    else:
        return JsonResponse({'error': 'Invalid request. Status parameter is missing.'}, status=400)


@login_required
def schair_data_view(request):
    latest_entry = SchairData.objects.latest('datetime')
    advice = Advice.objects.get(schair_data=latest_entry)

    activity = latest_entry.activity
    advice_text = advice.advice_text

    return render(request, 'schair_app/schair_data_view.html', {'activity': activity, 'advice': advice_text})


def update_data(request):
    latest_entry = SchairData.objects.latest('datetime')
    advice = Advice.objects.get(schair_data=latest_entry)

    activity = latest_entry.activity
    advice_text = advice.advice_text

    return JsonResponse({'activity': activity, 'advice': advice_text})


# Dashboard
from django.db.models import Count

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



# Machine learning
import joblib
import pandas as pd


# Load the trained model
clf = joblib.load('./ml_model/posture_classifier_model.joblib')

# Define the number of postures
num_postures = 4

# Create a dictionary to map posture labels to recommendations
recommendations = {
    'nor_recom': "Maintain your current posture. It's good!",
    'left_recom': "Adjust your posture to the middle from left. Consider stretching and changing positions.",
    'right_recom': "Adjust your posture to the middle from right. Consider stretching and changing positions.",
    'front_recom': "Adjust your posture to the middle. Breaking back, consider stretching and changing positions."
}

@csrf_exempt
def predict_posture(request):
    if request.method == 'POST' or request.method == 'GET':
        status = request.GET.get('status', None)

        if status is None:
            return JsonResponse({'error': 'Missing "status" parameter in the request.'}, status=400)

        try:
            posture_status = int(status)
            if posture_status not in range(1, num_postures + 1):
                return JsonResponse({'error': f'Invalid "status" value. It should be in the range 1 to {num_postures}.'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid "status" value. Please enter a numeric value.'}, status=400)

        # Save the received data to the database
        PostureData.objects.create(
            timestamp=timezone.now(),
            posture_status=posture_status,
        )

        # Retrieve the saved postures
        saved_postures = PostureData.objects.order_by('-timestamp')[:num_postures]
        num_saved_postures = len(saved_postures)

        if num_saved_postures == num_postures:
            # If there are at least four postures, make a prediction using the last four
            user_input = [entry.posture_status for entry in saved_postures][::-1]
            user_input_df = pd.DataFrame([user_input], columns=[f'Posture{i + 1}' for i in range(num_postures)])
            prediction = clf.predict(user_input_df)
            recommendation = recommendations.get(prediction[0], "Invalid posture recommendation.")

            # Clear the saved postures in the database
            PostureData.objects.all().delete()

            return JsonResponse({'prediction': prediction[0], 'recommendation': recommendation})

        return JsonResponse({'message': f'Posture {posture_status} saved successfully.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def popup(request):
    return render(request,'schair_app/popup.html')