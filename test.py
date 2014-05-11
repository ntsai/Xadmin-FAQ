#coding:utf-8
#!/usr/bin/env python
# from django.db import models
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from article.models import *
from share.models import *

s = ProjectInfo.objects.all()[0]
print s._meta.object_name
print s._meta.app_label

print models.get_models(s._meta.app_label,s._meta.object_name)
