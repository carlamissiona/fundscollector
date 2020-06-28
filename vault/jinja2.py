# from jinja2.environment import Environment
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.urls import reverse
#
# class JinjaEnvironment(Environment):
#     def __init__(self,**kwargs):
#         super(JinjaEnvironment, self).__init__(**kwargs)
#         self.globals['static'] = staticfiles_storage.url
#         self.globals['reverse'] = reverse


# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.urls import reverse
# from jinja2 import Environment
#
#
# def environment(**options):
#     env = Environment(**options)
#     env.globals.update({
#         'static': staticfiles_storage.url,
#         'url': reverse,
#     })
#     return env

pass
#
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.urls import reverse
# from jinja2 import Environment
# def environment(**options):
#     env = Environment(**options)
#     env.globals.update({
#         'static': staticfiles_storage.url,
#         'url': reverse,
#     })
#     return env
