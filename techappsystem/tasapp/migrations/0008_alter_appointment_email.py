from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0007_alter_hire_date_of_hire_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
