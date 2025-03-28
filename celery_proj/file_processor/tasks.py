from celery import shared_task
from .models import UploadedFile
from PyPDF2 import PdfReader
from celery_proj.celery import app

@shared_task
def process_file(file_id):
    file_obj = UploadedFile.objects.get(id=file_id)
    extracted_text = ""
    print("processing file...")
    try:
        with open(file_obj.file.path, "rb") as f:
                pdf = PdfReader(f)
                for page in pdf.pages:
                    extracted_text += page.extract_text() + "\n"

    except Exception as e:
        return f"Error processing file: {str(e)}"
    file_obj.result_text = extracted_text
    file_obj.processed = True
    file_obj.save()
    print("processing completed!!")
    return f"File {file_obj.file.name} processed successfully"

@shared_task
def cal_sum(x, y):
     print("testing...")
     return x+y