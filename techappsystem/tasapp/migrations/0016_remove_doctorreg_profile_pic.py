from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0015_techreg_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techreg',
            name='profile_pic',
        ),
    ]
