# Generated by Django 2.2.5 on 2020-04-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PicUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagefile', models.ImageField(blank=True, upload_to='pic_upload')),
            ],
        ),
    ]
