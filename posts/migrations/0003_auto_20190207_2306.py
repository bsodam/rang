# Generated by Django 2.1.5 on 2019-02-07 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20190207_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-time_created']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(choices=[('미국', '미국'), ('중국', '중국'), ('일본', '일본'), ('캐나다', '캐나다'), ('호주', '호주'), ('러시아', '러시아'), ('베트남', '베트남'), ('필리핀', '필리핀'), ('브라질', '브라질'), ('독일', '독일'), ('영국', '영국'), ('뉴질랜드', '뉴질랜드'), ('인도네시아', '인도네시아'), ('아르헨티나', '아르헨티나'), ('태국', '태국'), ('싱가포르', '싱가포르'), ('프랑스', '프랑스'), ('말레이시아', '말레이시아'), ('멕시코', '멕시코'), ('아랍에미리트', '아랍에미리트'), ('인도', '인도'), ('사우디아라비아', '사우디아라비아')], max_length=30),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Post'),
        ),
    ]