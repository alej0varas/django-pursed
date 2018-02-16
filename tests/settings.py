DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travis_ci_test',
        'USER': 'postgres',
        'HOST': 'localhost',
    }
}
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'wallet',
)
SITE_ID = 1
SECRET_KEY = 'this-is-just-for-tests-so-not-that-secret'
DEBUG = True
