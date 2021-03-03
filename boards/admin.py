from django.contrib import admin

# add Border section to admin panel
from boards.models import Board

admin.site.register(Board)

