from django.http import JsonResponse, HttpResponse
from cryptography.fernet import Fernet, MultiFernet
from .models import aws, log, dockerfile


def get_pwd(request):
    secret_key = Fernet.generate_key()
    key1 = Fernet(secret_key)
    f = MultiFernet([key1])
    myaws = aws.objects.all()[0]
    id = myaws.aid
    key = myaws.akey
    eid = f.encrypt(str.encode(id))
    ekey = f.encrypt(str.encode(key))
    print(eid)
    print(ekey)
    return JsonResponse({"aid": bytes.decode(eid), "akey": bytes.decode(ekey), "key": bytes.decode(secret_key)})


def log(request):
    return HttpResponse("1111111")


def get_dockerfile(request):
    df = dockerfile.objects.get(name=request.GET['name'])
    return HttpResponse(df.content)
