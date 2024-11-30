import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0s1+0f$p47ubn6c030x!qppn134)7gytkoi9z67dw(u*vuz5qi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allowed hosts for the application
ALLOWED_HOSTS = ["*"]

# REST Framework Configuration
REST_FRAMEWORK = {
    # Default authentication classes for the REST framework
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # Use JWT authentication for all API views
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # Default permission classes for the REST framework
    "DEFAULT_PERMISSION_CLASSES": [
        # Make all API views permission protected
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# Simple JWT Configuration
SIMPLE_JWT = {
    # Access token lifetime configuration
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),  # Access token lifetime: 30 minutes
    # Refresh token lifetime configuration
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),      # Refresh token lifetime: 1 day
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api', # Custom application
    'rest_framework', # Django REST framework
    'corsheaders', # Middleware for handling CORS
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', # CORS middleware
]

# URL configuration module
ROOT_URLCONF = 'backend.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # Directories to search for templates
        'APP_DIRS': True, # Enable loading templates from app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'backend.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Database engine
        'NAME': os.getenv("DB_NAME"), # Database file path
        'USER': os.getenv("DB_USER"), # Database username
        'PASSWORD': os.getenv("DB_PWD"), # Database password
        'HOST': os.getenv("DB_HOST"), # Database host
        'PORT': os.getenv("DB_PORT"), # Database port
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en-us' # Default language code
TIME_ZONE = 'UTC' # Default time zone
USE_I18N = True # Enable internationalization
USE_TZ = True # Enable time zone support

# Static files (CSS, JavaScript, Images) settings
STATIC_URL = 'static/' # URL for static files

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Default field type for primary keys

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins for CORS
CORS_ALLOW_CREDENTIALS = True   # Allow credentials in cross-site HTTP requests