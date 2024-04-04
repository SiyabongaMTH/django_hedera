from core.project.settings import ENV, DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV.config("SECRET_KEY")


from split_settings.tools import include
include(
    'base.py',
    'utils_config.py',
)

DEBUG = DEBUG

ALLOWED_HOSTS = ENV.config("ALLOWED_HOSTS", cast=ENV.Csv())
