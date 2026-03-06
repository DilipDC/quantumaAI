
from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_quantum_response
from .models import AIInteraction
import json
from django.views.decorators.csrf import csrf_exempt

def dashboard(request):
    return render(request, 'dashboard.html')

@csrf_exempt
def process_ai(request):

    if request.method == "POST":

        data = json.loads(request.body)

        prompt = data.get("prompt")
        deep = data.get("mode", False)

        result = get_quantum_response(prompt, deep)

        AIInteraction.objects.create(
            user_prompt=prompt,
            ai_response=result,
            mode="Deep" if deep else "Standard"
        )

        return JsonResponse({"response": result})
