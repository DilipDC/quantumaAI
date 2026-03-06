
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import get_quantum_response
from .models import AIInteraction
import json

def dashboard(request):
    return render(request,'dashboard.html')

@csrf_exempt
def process_ai(request):

    if request.method == "POST":
        data = json.loads(request.body)

        prompt = data.get("prompt")

        result = get_quantum_response(prompt)

        AIInteraction.objects.create(
            user_prompt=prompt,
            ai_response=result
        )

        return JsonResponse({"response": result})

    return JsonResponse({"response":"invalid request"})
