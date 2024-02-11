from django.http import JsonResponse
from PIL import Image
from transformers import ViltProcessor, ViltForQuestionAnswering
from django.views.decorators.csrf import csrf_exempt
 
@csrf_exempt
def get_answer(request):
    if request.method == 'POST':
        image_path = request.FILES['image']
        text = request.POST.get('question', 'Default question')
 
        # Open the image from the uploaded file
        image = Image.open(image_path)
 
        processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
        model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
 
        # Prepare inputs
        encoding = processor(image, text, return_tensors="pt")
 
        # Forward pass
        outputs = model(**encoding)
        logits = outputs.logits
        idx = logits.argmax(-1).item()
        predicted_answer = model.config.id2label[idx]
 
        return JsonResponse({'predicted_answer': predicted_answer})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)