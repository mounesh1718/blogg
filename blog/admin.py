from django.contrib import admin
from blog.models import Post,Category,Aboutus
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ('title','content')
    list_filter = ('category','created_at')
    
    
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Aboutus)


