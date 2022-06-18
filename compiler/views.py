from django.http import JsonResponse
from lib.java_runner import JavaRunner
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    user_dir = request.POST["user"]
    code = request.POST["code"]

    java_runner = JavaRunner(user_directory=user_dir, code=code)
    res = java_runner.run()

    return JsonResponse({
        'output': res
    }, status=200)
