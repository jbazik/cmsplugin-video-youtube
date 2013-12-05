#!/usr/bin/python
import os, sys
sys.path.append(os.path.abspath(os.path.join(
                os.path.dirname(__file__), os.pardir)))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
