from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

def schedule_setup():
    schedule, _ = IntervalSchedule.objects.get_or_create(
      period=IntervalSchedule.MINUTES, every=1
    )

    args=json.dumps([])

    PeriodicTask.objects.get_or_create(
      name="Send schedule",
      interval=schedule,
      task="movies.tasks.notify_of_starting_soon",
      args=args
    )
