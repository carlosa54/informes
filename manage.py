#!/usr/bin/env python
import os
import sys

import dotenv

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

if __name__ == "__main__":
	ENVIRONMENT = os.getenv('ENVIRONMENT')

	if ENVIRONMENT == 'STAGING':
		settings = 'staging'
	elif ENVIRONMENT == 'PRODUCTION':
		settings = 'production'
	else:
		settings = 'development'

	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "informes.settings")
	os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

	from configurations.management import execute_from_command_line

	execute_from_command_line(sys.argv)