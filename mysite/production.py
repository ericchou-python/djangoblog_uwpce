from settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['localhost', 'ec2-52-39-21-223.us-west-2.compute.amazonaws.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
