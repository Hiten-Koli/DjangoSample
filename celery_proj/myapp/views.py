from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .tasks import add, send_welcome_email
# Create your views here.


def home(request):
    task = add.delay(5, 10)
    print(f'{task}')
    return HttpResponse({f'"task_id": {task}, "status": "Task submitted"'})

@api_view(['POST'])
def register(request):
    user_email = request.data.get('email')
    if not user_email:
        return Response({"error": "Email is required"}, status=400)

    # Send email asynchronously using Celery
    send_welcome_email.delay(user_email)

    return Response({"message": "User registered, email will be sent in the background!"})