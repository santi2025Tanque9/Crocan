from .base import *

# SECURITY WARNING: don't run with debug turned on in production!


DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbcrocan',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'


STATICFILES_DIRS = [BASE_DIR / 'static']
# Para que Django sepa dónde guardar los archivos subidos y cómo servirlos, debes agregar dos configuraciones clave en tu archivo settings.py
MEDIA_URL = '/media/' #Es la URL base que se utilizará para acceder a estos archivos desde el navegador
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #Es la ruta absoluta en tu sistema de archivos donde se almacenarán los archivos subidos.


# Para probar localmente por la consola si se esta realizando bien el cambio de contraseña
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'