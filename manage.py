#!/usr/bin/env python
import sys

def main():
    from django.conf import settings

    if not settings.configured:
        settings.configure(
            INSTALLED_APPS=['django_google_adwords'],
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
        )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
