#!/usr/bin/env python
import django
import logging
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from os.path import abspath, dirname

APP_NAME = 'ambition_visit_schedule'


class DisableMigrations:

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


installed_apps = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'django_crypto_fields.apps.AppConfig',

    'edc_action_item.apps.AppConfig',
    'edc_appointment.apps.AppConfig',
    'edc_base.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_metadata.apps.AppConfig',
    'edc_notification.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',

    'ambition_labs.apps.AppConfig',
    'ambition_lists.apps.AppConfig',
    'ambition_screening.apps.AppConfig',
    'ambition_subject.apps.AppConfig',

    f'{APP_NAME}.apps.AppConfig',
]

DEFAULT_SETTINGS = dict(
    BASE_DIR=dirname(dirname(abspath(__file__))),
    ALLOWED_HOSTS=['localhost'],
    # AUTH_USER_MODEL='custom_user.CustomUser',
    ROOT_URLCONF=f'{APP_NAME}.tests.urls',
    STATIC_URL='/static/',
    INSTALLED_APPS=installed_apps,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        },
    },
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'edc_dashboard.middleware.DashboardMiddleware',
        'edc_subject_dashboard.middleware.DashboardMiddleware',
    ],

    LANGUAGE_CODE='en-us',
    TIME_ZONE='UTC',
    USE_I18N=True,
    USE_L10N=True,
    USE_TZ=True,

    APP_NAME=f'{APP_NAME}',
    DASHBOARD_URL_NAMES={},
    EDC_BOOTSTRAP=3,
    EMAIL_CONTACTS={},
    EMAIL_ENABLED=False,
    SITE_ID=10,

    DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage',
    MIGRATION_MODULES=DisableMigrations(),
    PASSWORD_HASHERS=('django.contrib.auth.hashers.MD5PasswordHasher', ),

)


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    failures = DiscoverRunner(failfast=True).run_tests(
        [f'{APP_NAME}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
