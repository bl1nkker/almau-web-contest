from django.db import models

# Create your models here.


class ContestTeam(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100, default='0')


class ContestParticipant(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(ContestTeam, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, default='000-000-0000')
    is_active = models.BooleanField(default=True)
    is_leader = models.BooleanField(default=False)


class ContestTask(models.Model):
    description = models.CharField(max_length=100)
    score = models.IntegerField()


class ContestTeamCertificate(models.Model):
    team = models.ForeignKey(ContestTeam, on_delete=models.CASCADE)
    place = models.IntegerField()
    desciption = models.CharField(max_length=100)


class ContestParticipantCertificate(models.Model):
    participant = models.ForeignKey(
        ContestParticipant, on_delete=models.CASCADE)
    place = models.IntegerField()
    desciption = models.CharField(max_length=100)
