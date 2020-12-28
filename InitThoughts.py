import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'MindChange.settings')

import django
django.setup()
from thoughtReverse.models import Thought

def Init():
    # thoughts = {'You are not good enough.': 'You are always good enough.',
    #             'They were laughing at me.': 'They forgot the whole thing the next day.',
    #             'I am nervous.': 'I care about it.',}

    thoughts = {'我不够优秀。': '我已经比许多人都优秀了。',
                '他们在笑我。': '他们第二天就全忘了。',
                '我很紧张。': '我在意这件事，这很好。',
                '我不知道生命的意义。': '我迟早会知道生命的意义。',}

    negatives = list(thoughts.keys())
    positives = list(thoughts.values())

    for i in range(len(thoughts)):
        t = Thought.objects.get_or_create(negative=negatives[i], positive=positives[i])[0]
        t.save()

if __name__ == '__main__':
    print("Initializing...")
    Init()