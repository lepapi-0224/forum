from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Board(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True
    )
    description = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )


class Topic(models.Model):
    subject = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    last_updated = models.DateTimeField(
        auto_now_add=True
    )
    board = models.ForeignKey(
        Board,
        related_name='topics',
        on_delete=models.DO_NOTHING
    )
    starter = models.ForeignKey(
        User,
        related_name='topics',
        on_delete=models.DO_NOTHING
    )


class Post(models.Model):
    message = models.TextField(
        max_length=4000,
        null=False,
        blank=False
    )
    topic = models.ForeignKey(
        Topic,
        related_name='posts',
        on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        null=True
    )
    created_by = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.DO_NOTHING
    )
    updated_by = models.ForeignKey(
        User,
        null=True,
        related_name='+',
        on_delete=models.DO_NOTHING
    )