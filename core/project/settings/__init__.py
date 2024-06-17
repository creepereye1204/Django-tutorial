import os.path
from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

ENVVAR_SETTING_PREFIX = 'CORESETTINGS_'

LOCAL_SETTINGS_PATH = os.getenv(f'{ENVVAR_SETTING_PREFIX}LOCAL_SETTINGS_PATH')

if os.getenv(f'{ENVVAR_SETTING_PREFIX}IN_DOCKER'):
    IN_DOCKER = True

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = 'local/settings.dev.py'

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)

include('base.py', 'logger.py', 'custom.py', optional(LOCAL_SETTINGS_PATH), 'envvars.py', 'docker.py')
