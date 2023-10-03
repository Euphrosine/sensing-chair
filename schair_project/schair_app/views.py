from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SchairData
from datetime import datetime
from django.shortcuts import render


class SchairDataAPI(APIView):
    def post(self, request):
        # Assuming you receive 'status' in the request data
        status_code = request.data.get('status', 0)
        
        if status_code == 1:
            activity = "A person is bending to the left side of a chair"
        elif status_code == 2:
            activity = "A person is bending to the right side of a chair"
        elif status_code == 3:
            activity = "A person is seated wrongly in the central position of a chair"
        else:
            activity = "No activity"
            
        SchairData.objects.create(datetime=datetime.now(), activity=activity)
        return Response({'message': 'Data recieved successfully'}, status=status.HTTP_201_CREATED)



def schair_data_view(request):
    schair_data = SchairData.objects.all()
    return render(request, 'schair_app/schair_data.html', {'schair_data': schair_data})
