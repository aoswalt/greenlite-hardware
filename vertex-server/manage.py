#!/usr/bin/env python
import os
import sys
import signals

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vertex.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    # start threads for scheduale processing and lighting if not running and on main thread
    if sys.argv[1] == 'runserver' and os.environ.get('RUN_MAIN') != 'true':
        print('Starting threads')
        signals.schedule.start()
        signals.lights.start()

    execute_from_command_line(sys.argv)
