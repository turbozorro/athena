from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserSubject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_tasks = models.IntegerField(default=0)
    completed_tasks = models.IntegerField(default=0)
    completion = models.FloatField(default=0)
    grade = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])


class Task(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    completion = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])

    class Meta:
        unique_together = ('user', 'task')

    @property
    def name(self):
        return self.task.name

    def __str__(self):
        return self.name
