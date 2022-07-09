"""
Django settings for luffycityapi project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 主应用目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 将 apps 目录加入 sys.path 便于路径识别和导包
sys.path.insert(0, str(BASE_DIR / "apps"))
sys.path.insert(0, str(BASE_DIR / "utils"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1p6%@lpn(+3_wpse-7_q+jd%zc(o-t+2(1y3!eczbqw_e+hrql'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 添加rest_framework模块
    "rest_framework",
    # cors 跨域子应用
    'corsheaders',

    'home',
    'users',
]

MIDDLEWARE = [
    # 跨域中间件 在 CommonMiddleware 上面即可
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ORIGIN_WHITELIST = (
#     'http:127.0.0.1:3000',
# )

# 不允许 ajax 跨域请求时携带 cookie
# CORS_ALLOW_CREDENTIALS = False

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'luffycityapi.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'luffycityapi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# 配置数据库
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    # 默认数据库配置
    'default': {
        'ENGINE': 'dj_db_conn_pool.backends.mysql',
        'NAME': 'luffycity',
        'PORT': 3306,
        'HOST': '127.0.0.1',
        'USER': 'luffycity_user',
        'PASSWORD': 'luffycity',
        'OPTIONS': {
            # 连接选项配置 mysql8.0以上无需配置
            'charset': 'utf8mb4'
        },
        # 连接池配置
        'POOL_OPTIONS': {
            # 连接池默认创建的链接对象的数量
            'POOL_SIZE': 10,
            # 连接池默认创建的链接对象的最大数量
            'MAX_OVERFLOW': 10
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# 设置django的静态文件目录【手动创建】
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# 项目中存储上传文件的根目录【手动创建】
MEDIA_ROOT = BASE_DIR / "uploads"
# 访问上传文件的url地址前缀
MEDIA_URL = "/uploads/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 日志配置
LOGGING = {
    # 使用的日志模块的版本
    'version': 1,
    # 是否禁用其他的已经存在的日志功能
    'disable_existing_loggers': False,
    # 日志格式设置 verbose或者simple都是自定义的
    'formatters': {
        # 详细格式，适用于开发人员不在场的情况下的日志记录
        # levelname 日志等级
        # asctime 发生时间
        # module 文件名
        # process 进程id
        # thread 线程id
        # message 异常信息
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',  # 变量格式分隔符
        },
        # 简单格式，适用于开发人员在场的情况下的终端输出
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    # 过滤器
    'filters': {
        # 就是上面的 DEBUG=True 配置
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 日志处理流程，console或者mail_admins都是自定义的
    'handlers': {
        'console': {
            'level': 'DEBUG',  # 设置当前的日志处理流程中的日志最低等级
            # 当前日志处理流程的日志过滤
            'filters': ['require_debug_true'],
            # 当前日志处理流程的核心类 StreamHandler 可以帮助我们把日志信息输出到终端
            'class': 'logging.StreamHandler',
            # 当前日志处理流程的日志格式
            'formatter': 'simple'
        },
        # 输出到邮件
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     'filters': ['special']
        # }
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置 ，日志文件名，日志保存目录logs必须手动创建
            'filename': BASE_DIR.parent / 'logs/luffycity.log',
            # 单个日志文件的最大值，这里 我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 备份日志文件的数量，设置最大日志数量为10
            'backupCount': 10,
            # 日志格式： 详细格式
            'formatter': 'verbose'
        }
    },
    # 日志处理的命名空间
    'loggers': {
        'django': {
            # 当前django命名空间写入日志时，调用哪几个日志处理流程
            'handlers': ['console', 'file'],
            # 是否在django命名空间对应的日志处理流程结束以后，冒泡通知其他的日志功能
            'propagate': True,
        },
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': False,
        # },
        # 'myproject.custom': {
        #     'handlers': ['console', 'mail_admins'],
        #     'level': 'INFO',
        #     'filters': ['special']
        # }
    }
}

# drf 配置
REST_FRAMEWORK = {
    # 自定义异常处理
    'EXCEPTION_HANDLER': 'luffycityapi.utils.exceptions.custom_exception_handler',
}

# redis configration
# 设置redis缓存
CACHES = {
    # 默认缓存
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 项目上线时,需要调整这里的路径
        # "LOCATION": "redis://:密码@IP地址:端口/库编号",
        "LOCATION": "redis://:@127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    },
    # 提供给admin运营站点的session存储
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:@127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 10},
        }
    },
    # 提供存储短信验证码
    "sms_code": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:@127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 10},
        }
    }
}

# 设置用户登录admin站点时,记录登录状态的session保存到redis缓存中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 设置session保存的位置对应的缓存配置项
SESSION_CACHE_ALIAS = "session"

# 告诉django 系统认证相关的功能用户模型类采用自定义的用户模型类
# 格式：子应用目录名.模型类名
AUTH_USER_MODEL = "users.User"
