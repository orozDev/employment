"""
Django settings for employment project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os, pytz

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-maylyjq$g&)j9_o7qoqpt&my5(g_vyfmq1cn^ezp85!4!*7opv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'corsheaders',
    'django_cleanup',
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
    'django_filters',
    'core',
    'summary',
    'company',
    'hiring',
    'freelance',
    'pricing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'employment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'employment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'employment',
        'USER': 'oroz',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


CORS_ORIGIN_ALLOW_ALL = True   

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# CORS_ORIGIN_WHITELIST = (
#        'http://127.0.0.1:3000/',
# )

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        #'oauth2_provider.ext.rest_framework.OAuth2Authentication',  # django-oauth-toolkit < 1.0.0
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
        'drf_social_oauth2.authentication.SocialAuthentication',
    ],
}

AUTHENTICATION_BACKENDS = (

    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '760676748693779'
SOCIAL_AUTH_FACEBOOK_SECRET = '0abc06f9dce2b3e201cff6291bfd61de'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

# Google configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1013567575080-9j0cl3g6fphb26nnqeo9msrgdood1jb7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

SOCIAL_AUTH_USER_FIELDS = ['email', 'username', 'first_name', 'last_name', 'gender', 'password', 'avatar']

# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

timezones = pytz.all_timezones
TIME_ZONE = 'Etc/GMT-6'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.Users'


JAZZMIN_SETTINGS = {
    # заголовок окна (по умолчанию будет current_admin_site.site_title, если он отсутствует или отсутствует)
    "site_title": "Employment Admin",

    # Заголовок на экране входа (максимум 19 символов) (по умолчанию — current_admin_site.site_header, если он отсутствует или отсутствует)
    "site_header": "Employment.kg",

    # Название бренда (максимум 19 символов) (по умолчанию — current_admin_site.site_header, если оно отсутствует или отсутствует)
    "site_brand": "Employment Admin",

    # Логотип для вашего сайта должен присутствовать в статических файлах, используется для бренда в левом верхнем углу.
    "site_logo": '/img/main_logo.gif',

    # Классы CSS, которые применяются к логотипу выше
    "site_logo_classes": "",

    # Относительный путь к значку для вашего сайта, по умолчанию будет site_logo, если он отсутствует (в идеале 32x32 px)
    "site_icon": '/img/logo.png',

    # Приветственный текст на экране входа
    "welcome_sign": "Добро пожаловать в администрацию сайта",

    # Авторское право на нижний колонтитул
    "copyright": "OROZ",

    # Администратор модели для поиска из панели поиска, панель поиска опускается, если исключена
    "search_model": "core.Users",

    # Имя поля в модели пользователя, которое содержит аватар ImageField/URLField/Charfield или вызываемый объект, который получает пользователя
    "user_avatar": 'avatar',

    ############
    # Top Menu #
    ############

    # Ссылки для размещения в верхнем меню
    "topmenu_links": [

        # URL-адрес, который становится обратным (можно добавить разрешения)
        {"name": "Главная",  "url": "admin:index",
            "permissions": ["auth.view_user"]},

        # внешний URL, который открывается в новом окне (можно добавить разрешения)
        #{"name": "Jazzmin", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"name": "Rest API", "url": "/api/swagger", "new_window": False},

        # Приложение с выпадающим меню для всех страниц своих моделей (разрешения проверены для моделей)
        #{"app": "books"},
    ],

    #############
    # Меню пользователя#
    #############

    # Дополнительные ссылки для включения в меню пользователя в правом верхнем углу (URL-адрес типа "приложение" не разрешен)
    "usermenu_links": [
    ],

    #############
    # Боковое меню #
    #############

    # Отображать ли боковое меню
    "show_sidebar": True,

    # Нужно ли автоматически расширять меню
    "navigation_expanded": True,

    # Скрыть эти приложения при создании бокового меню, например (авторизация)
    "hide_apps": [],

    # Скрыть эти модели при создании бокового меню (например, auth.user)
    "hide_models": [],

    # Список приложений (и/или моделей) для базового упорядочения бокового меню (не обязательно содержать все приложения/модели)
    "order_with_respect_to": [
  
    ],

    # Пользовательские ссылки для добавления в группы приложений, вводимые по имени приложения
    # "custom_links": {
    #     "Products": [{
    #         "name": "Make dssdfsdfdsfdfdddddddddddddddddddddddddddddddddddddddd Messages",
    #         "url": "make_messages",
    #         "icon": "fas fa-comments",
    #         "permissions": ["books.view_book"]
    #     }]
    # },

    # Пользовательские значки для приложений/моделей бокового меню См. https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # полный список бесплатных классов значков 5.13.0
    "icons": {
       'auth.Group': 'fas fa-users',
        'core.Users': 'fas fa-user',
        'hiring.Hiring': 'fas fa-binoculars',
        'hiring.Tags': 'fas fa-tags',
        'summary.Skills': 'fas fa-check',
        'summary.Citizenships': 'far fa-flag',
        'summary.Education': 'fas fa-user-graduate',
        'summary.ForeignLanguages': 'fas fa-language',
        'summary.JobExperience': 'fas fa-business-time',
        'company.Companies': 'far fa-building',
        'summary.Occupations': "fas fa-user-tie",
        'summary.Summaries': 'fas fa-clipboard-list',
        'rest_framework.authtoken.token': 'fas fa-users',
        
        'freelance.Orders':'far fa-folder',
    
        'rest_framework.authtoken.TokenProxy': 'fas fa-key'
    },
    # Значки, которые используются, если они не указаны вручную
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Связанный модальный #
    #################
    # Используйте модальные окна вместо всплывающих окон
    "related_modal_active": False,

    #############
    # Настройки пользовательского интерфейса #
    #############
    # Относительные пути к пользовательским скриптам CSS/JS (должны присутствовать в статических файлах)
    "custom_css": None,
    "custom_js": '/js/admin_script.js',
    # Показывать ли настройщик пользовательского интерфейса на боковой панели
    "show_ui_builder": True,

    ###############
    # Сменить вид #
    ###############
    # Визуализировать представление изменений в виде отдельной формы или на вкладках, текущие параметры
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # переопределить формы изменений для каждой модели на основе администратора
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},

}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-danger",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}
