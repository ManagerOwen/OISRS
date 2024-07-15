from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0005_alter_customuser_user_type_hire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(3, 'User'), (1, 'admin'), (2, 'tec')], default=1, max_length=50),
        ),
    ]
