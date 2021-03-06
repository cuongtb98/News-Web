# Generated by Django 3.2.2 on 2021-05-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('keyword', models.TextField()),
                ('description', models.TextField()),
                ('summary', models.TextField()),
                ('category', models.SmallIntegerField(choices=[(0, 'Chính trị xã hội'), (1, 'Đời sông'), (2, 'Thể Thao'), (3, 'Sức khỏe'), (4, 'Khoa học'), (5, 'Du lịch')])),
            ],
        ),
    ]
