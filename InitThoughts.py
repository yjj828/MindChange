import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'MindChange.settings')

import django
django.setup()
from thoughtReverse.models import Thought

def Init():
    thoughts = {'You are not good enough.': 'You are always good enough.',
                'They were laughing at me.': 'They forgot the whole thing the next day.',
                'I am nervous.': 'I care about it.',}

    negatives = list(thoughts.keys())
    positives = list(thoughts.values())

    for i in range(len(thoughts)):
        t = Thought.objects.get_or_create(negative=negatives[i], positive=positives[i])[0]
        t.save()

if __name__ == '__main__':
    print("Initializing...")
    Init()