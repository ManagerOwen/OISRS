from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0008_alter_hire_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='description',
            field=models.ImageField(null=True, upload_to='description/customer_pres'),
        ),
        migrations.AddField(
            model_name='hire',
            name='remark',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='hire',
            name='status',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
