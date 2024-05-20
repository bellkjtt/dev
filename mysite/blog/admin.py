from django.contrib import admin
from .models import  * #가져오려는 모델을 먼저 가져와서 import 해준다.

admin.site.register(Post) #
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Tag)