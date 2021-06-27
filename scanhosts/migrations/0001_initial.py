# Generated by Django 3.2.4 on 2021-06-26 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserIPInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='', max_length=40, null=True, verbose_name='IP地址')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户访问地址信息表',
                'verbose_name_plural': '用户访问地址信息表',
                'db_table': 'user_ip_info',
            },
        ),
        migrations.CreateModel(
            name='BrowseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useragent', models.CharField(default='', max_length=100, null=True, verbose_name='用户浏览器agent信息')),
                ('userIp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanhosts.useripinfo')),
            ],
            options={
                'verbose_name': '用户浏览器信息表',
                'verbose_name_plural': '用户浏览器信息表',
                'db_table': 'browse_info',
            },
        ),
    ]