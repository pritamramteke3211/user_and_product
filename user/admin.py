from django.contrib import admin
from .models import User,Post,PostComment

# Register your models here.
admin.site.register(User)

class PostCommentInline(admin.TabularInline):
    model = PostComment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','created_at','updated_at']
    inlines = [PostCommentInline]

