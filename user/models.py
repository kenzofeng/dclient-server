from django.db import models


class aws(models.Model):
    aid = models.CharField(max_length=100)
    akey = models.CharField(max_length=100)


class log(models.Model):
    ip = models.CharField(max_length=20)
    content = models.TextField()


class dockerfile(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()


class Access(models.Model):
    docker_registry = models.CharField(max_length=200)
    user = models.CharField(max_length=100)
    pwd = models.CharField(max_length=500)
