from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0010_alter_hire_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='recommendedrepair',
            field=models.TextField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='hire',
            name='description',
            field=models.TextField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'tec'), (3, 'User')], default=1, max_length=50),
        ),
    ]
