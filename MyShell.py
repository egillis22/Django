import os 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django 

django.setup()

from MainApp.models import Topic
topics = Topic.objects.all()

for t in topics:
    print(f"Topic ID: {t.id} and Topic Name: {t}")

from MainApp.models import Entry
entries = Entry.objects.all()

t = Topic.objects.get(id=1)
print(t)
entry = t.entry_set.all()
print(entry)
'''
for e in entries:
    print(f"Topic: {e.topic}")
    print(f"Entry: {e.text}")
'''
