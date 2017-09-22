#!/usr/bin/env python
import os
import sys
import django
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lujunxu.settings")
    argv = ['manage.py', 'migrate']
    execute_from_command_line(argv)
