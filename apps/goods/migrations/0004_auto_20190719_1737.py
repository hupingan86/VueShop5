# Generated by Django 2.2.3 on 2019-07-19 17:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20190709_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
            },
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterModelOptions(
            name='goodsimage',
            options={'verbose_name': '商品图片', 'verbose_name_plural': '商品图片'},
        ),
        migrations.RemoveField(
            model_name='goodsimage',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_front_image',
            field=models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='是否热销'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='是否新品'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=100, verbose_name='商品名'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='sold_num',
            field=models.IntegerField(default=0, verbose_name='商品销售量'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='desc',
            field=models.TextField(default='', help_text='类别描述', verbose_name='类别描述'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='image',
            field=models.ImageField(max_length=200, upload_to='brands/'),
        ),
        migrations.AlterModelTable(
            name='goodscategorybrand',
            table='goods_goodsbrand',
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='goods.GoodsCategory', verbose_name='商品类目')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Goods')),
            ],
            options={
                'verbose_name': '首页商品类别广告',
                'verbose_name_plural': '首页商品类别广告',
            },
        ),
    ]