from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0011_hire_recommendedrepair_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'tec')], default=1, max_length=50),
        ),
    ]
