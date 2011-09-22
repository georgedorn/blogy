THEME = 'lifebook'

MARKITUP_FILTER = ('markitup.renderers.render_rest', {})
MARKITUP_SET = 'markitup/sets/restructuredtext'
MARKITUP_SKIN = 'markitup/skins/markitup'
MARKITUP_AUTO_PREVIEW = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
    'django.contrib.markup',
    'blogy',
    'markitup',
    'taggit',
)
