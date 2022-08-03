from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # display the properties mentioned in the tuple
    list_display = ('title', 'slug', 'status', 'created_on')
    # add the filtering by status
    list_filter = ('status',)
    # add the search bar which will search the data considering the attributes of this field
    search_fields = ['title', 'content']
    # to create automatically the slug based on the title
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
