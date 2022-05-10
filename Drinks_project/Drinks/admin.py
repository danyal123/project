import imp
from multiprocessing.spawn import import_main_path
from django.contrib import admin
from .Models import Drinks

admin.site.register(Drinks)