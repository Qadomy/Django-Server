from django.contrib import admin
# add Border section to admin panel
from django.contrib.auth.models import Group

from boards.models import Board, Topic


class InlineTopic(admin.StackedInline):
    model = Topic
    extra = 1


class BoardAdmin(admin.ModelAdmin):
    inlines = [InlineTopic]


class TopicAdmin(admin.ModelAdmin):
    fields = ('subject', 'board', 'created_by', 'views')
    list_display = ('subject', 'board', 'created_by', 'combine_subject_and_board')
    list_display_links = ('board', 'created_by')
    list_editable = ('subject',)
    list_filter = ('created_by', 'board')
    search_fields = ('board', 'created_by')

    @staticmethod
    def combine_subject_and_board(obj):
        return "{} - {}".format(obj.subject, obj.board)


# register
admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)
#  unregister
admin.site.unregister(Group)

# name
admin.site.site_header = "Boards Admin Panel"
admin.site.site_title = "Boards Admin Panel"
