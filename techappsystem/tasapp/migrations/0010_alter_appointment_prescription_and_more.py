from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0009_hire_descrption_hire_remark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='descrption',
            field=models.FileField(null=True, upload_to='pdfs/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(3, 'User'), (1, 'admin'), (2, 'doc')], default=1, max_length=50),
        ),
    ]
