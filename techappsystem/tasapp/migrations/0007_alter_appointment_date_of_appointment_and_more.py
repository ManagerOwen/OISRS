from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0006_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='date_of_hire',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hire',
            name='time_of_hire',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'tec'), (1, 'admin'), (3, 'User')], default=1, max_length=50),
        ),
    ]
