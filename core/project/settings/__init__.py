import os
from pathlib import Path
from split_settings.tools import include

#Decouple
from decouple import Csv, config
from dotmap import DotMap

#init environment
ENV = DotMap({"config": config,"Csv": Csv})





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ADMIN_PATH = ENV.config("ADMIN_PATH")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV.config("DEBUG", cast=bool)


include(
    'base.py',
    'utils_config.py',
)
if DEBUG:
    include("development.py")
else:
    include("production.py")