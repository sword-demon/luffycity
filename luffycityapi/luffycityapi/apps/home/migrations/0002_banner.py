# Generated by Django 3.2.9 on 2022-07-03 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='名称/标题')),
                ('orders', models.IntegerField(default=0, verbose_name='排序')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否在前端显示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除了')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('image', models.ImageField(upload_to='banner/%Y/', verbose_name='图片地址')),
                ('link', models.CharField(max_length=500, verbose_name='链接地址')),
                ('note', models.CharField(max_length=150, verbose_name='备注信息')),
                ('is_http', models.BooleanField(default=False, help_text='站点链接: http://www.baidu.com/book/', verbose_name='是否外网链接')),
            ],
            options={
                'verbose_name': '轮播广告',
                'verbose_name_plural': '轮播广告',
                'db_table': 'lf_banner',
            },
        ),
    ]
