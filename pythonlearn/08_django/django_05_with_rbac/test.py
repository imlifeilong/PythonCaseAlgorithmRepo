from authxs.models import User

u = User.objects.create_user(username="lifeilong", password="lifeilong")
u.save()


u = User.objects.get(username='lifeilong')
u.set_password('admin123!')
u.save()


u = User.objects.get(username='root')