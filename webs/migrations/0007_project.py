# Generated by Django 2.1.5 on 2019-05-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0006_auto_20190122_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='images/')),
                ('short_des', models.TextField()),
                ('full_des', models.TextField(null=True)),
                ('title', models.TextField(null=True)),
                ('references', models.TextField(null=True)),
                ('ongoing', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
            ],
        ),
    ]
