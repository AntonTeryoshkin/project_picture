# Generated by Django 3.1.2 on 2020-10-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/Images/files'),
        ),
    ]