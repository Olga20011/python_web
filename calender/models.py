from django.db import models
from django.urls import reverse

# Create your models here.
class Events(models.Model):
    event_name=models.CharField(max_length=20,null=True)
    start_time=models.DateField(null=True)
    end_time=models.DateField(null=True)
    guests=models.CharField(max_length=20,null=True)
    event_task=models.CharField(max_length=20,null=True)
    venue=models.CharField(max_length=20,null=True)
    event_id=models.CharField(max_length=20,null=True)
    duration=models.DurationField(null=True)

    @property
    def get_html_url(self):
        url = reverse('calender:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'





