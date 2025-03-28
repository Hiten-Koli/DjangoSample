from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from .tasks import process_file, cal_sum

# Create your views here.

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            file_obj = serializer.save()
            #Celery task
            task = process_file.delay(file_obj.id)
            task.wait()
            return Response({
                "message": "File uploaded successfully, processing started!",
                "task_id": task.id,
                "file_id": file_obj.id
            }, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileStatusView(APIView):
    def get(self, request, file_id):
        try:
            file_obj = UploadedFile.objects.get(id=file_id)
            return Response({
                "file": file_obj.file.name,
                "processed": file_obj.processed,
                "result_text": file_obj.result_text
            }, status.HTTP_200_OK)
        except UploadedFile.DoesNotExist:
            return Response({'error': 'File Not Found'}, status.HTTP_404_NOT_FOUND)
        
class SumView(APIView):
    def get(self, request):
        result = cal_sum.delay(10, 20)
        result.wait()
        print(result.result)
        print("Task done")
        return Response({f'Sum called'}, status.HTTP_200_OK)
