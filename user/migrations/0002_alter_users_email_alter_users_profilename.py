# Generated by Django 4.1.3 on 2022-11-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(error_messages={'unique': '이미 사용중인 이메일입니다'}, max_length=254, unique=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='users',
            name='profilename',
            field=models.CharField(error_messages={'unique': 'profilename은 필수항목입니다'}, max_length=30, verbose_name='회원이름'),
        ),
    ]
