from django.contrib import admin
from .models import Answer, FeedBack, Question, Notification

# Register your models here.

admin.site.register(Answer)
admin.site.register(FeedBack)
admin.site.register(Question)
admin.site.register(Notification)
