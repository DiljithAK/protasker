from django.http import JsonResponse
from .models import Tasks
from .serializers import TaskSerializer

def task_list(request):
    tasks = Tasks.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)