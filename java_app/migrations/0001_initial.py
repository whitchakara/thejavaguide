# Generated by Django 2.2 on 2021-11-13 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JavaShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField()),
                ('hours_of_operation', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambience', models.IntegerField()),
                ('cleanliness', models.IntegerField()),
                ('coffee', models.IntegerField()),
                ('music', models.IntegerField()),
                ('location', models.IntegerField()),
                ('additonal_comments', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('java_shops', models.ManyToManyField(related_name='shops', to='java_app.JavaShop')),
            ],
        ),
        migrations.AddField(
            model_name='javashop',
            name='reviews',
            field=models.ManyToManyField(related_name='reviews', to='java_app.Review'),
        ),
    ]
