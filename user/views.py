from django.http import JsonResponse, HttpResponse
from cryptography.fernet import Fernet
from .models import aws, log, dockerfile, Access

secret_key = b'XQYfjn2t4BkYHsTpkPZDzfSlLQqAJGzEzF8GPkEYjfc='


def log(request):
    return HttpResponse("1111111")


def get_dockerfile(request):
    df = dockerfile.objects.get(name=request.GET['name'])
    return HttpResponse(df.content)


def get_access(request):
    access = Access.objects.get(docker_registry=request.GET['docker_registry'])
    user = access.user
    pwd = access.pwd
    cipher_suite = Fernet(secret_key)
    en_user = cipher_suite.encrypt(str.encode(user))
    en_pwd = cipher_suite.encrypt(str.encode(pwd))
    return JsonResponse({"u": bytes.decode(en_user), "p": bytes.decode(en_pwd)})
