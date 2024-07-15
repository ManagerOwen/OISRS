from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0014_remove_techreg_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='techrreg',
            name='profile_pic',
            field=models.ImageField(default=0, upload_to='media/profile_pic'),
        ),
    ]
