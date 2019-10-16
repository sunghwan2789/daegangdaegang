from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    location = models.CharField(max_length=20)	# 강의실 건물
    floor = models.IntegerField()			# 강의실 층
    class_number = models.CharField(max_length=10)			# 강의실 번호
    tools = models.CharField(max_length=20) # 비품 목록
    people_number = models.IntegerField()          # 수용 인원

    def __str__(self):
        return self.class_number

class Reserve(models.Model):
    """
    예약 현황을 나타내는 모델

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return '[%s] %s : %s ~ %s' % (self.room, self.user.username, self.start_time, self.end_time)
# Create your models here.
