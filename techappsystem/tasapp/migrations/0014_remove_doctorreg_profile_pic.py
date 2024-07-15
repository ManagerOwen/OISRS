from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0013_page_alter_customuser_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techreg',
            name='profile_pic',
        ),
    ]
