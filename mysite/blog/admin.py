from django.contrib import admin
from .models import Post


# it is a subclass used to customize the admin app's interface of the model
class PostAdmin(admin.ModelAdmin):
    # display the properties mentioned in the tuple
    list_display = ('title', 'slug', 'status', 'created_on')
    # add the filtering by status
    list_filter = ('status',)
    # add the search bar which will search the data considering the attributes of this field
    search_fields = ['title', 'content']
    # to create automatically the slug based on the title
    prepopulated_fields = {'slug': ('title',)}


# it makes the model Post available to the admin app with its customizations
admin.site.register(Post, PostAdmin)
