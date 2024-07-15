from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (3, 'User'), (2, 'doc')], default=1, max_length=50),
        ),
    ]
