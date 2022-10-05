from django.contrib import admin
from contest_app.models import ContestParticipant, ContestTeam, ContestTask, ContestTeamCertificate, ContestParticipantCertificate
# Register your models here.

admin.site.register(ContestParticipant)
admin.site.register(ContestTeam)
admin.site.register(ContestTask)
admin.site.register(ContestTeamCertificate)
admin.site.register(ContestParticipantCertificate)
