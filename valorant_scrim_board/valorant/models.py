from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Rank(models.Model):
    name = models.CharField(verbose_name='ランク帯', max_length=10)
    
    def __str__(self):
        return self.name

User = get_user_model()

class Board(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_name = models.CharField(verbose_name='チームネーム', max_length=40, null=True)
    start_at = models.DateTimeField(verbose_name='開始日時', default=timezone.now)
    average_rank = models.ManyToManyField(Rank, verbose_name='ランク', max_length=40)
    map = models.CharField(verbose_name='マップ', max_length=40)
    comment = models.TextField(verbose_name='コメント', max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)

