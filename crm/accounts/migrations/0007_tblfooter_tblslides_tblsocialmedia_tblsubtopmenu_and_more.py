# Generated by Django 5.1.2 on 2024-12-14 14:30

import ckeditor_uploader.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_tblclients'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footerName', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tblSlides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slideName', models.CharField(max_length=200, null=True)),
                ('slideImage', models.ImageField(null=True, upload_to='images/')),
                ('slideDescription', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('active', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tblSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socialMediaName', models.CharField(max_length=200, null=True)),
                ('socialMediaURL', models.CharField(max_length=200, null=True)),
                ('socialMediaImage', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tblSubTopMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subTopMenuName', models.CharField(max_length=200, null=True)),
                ('subTopMenuImage', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tblTopMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topMenuName', models.CharField(max_length=200, null=True)),
                ('topMenuImage', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tblclients',
            name='clientDescription',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.CreateModel(
            name='tblProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productDetailName', models.CharField(max_length=200, null=True)),
                ('productDetailDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('productSize', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('productColor', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('productID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.tblproducts')),
            ],
        ),
        migrations.CreateModel(
            name='tblProductDetailImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productDetailImageName', models.CharField(max_length=200, null=True)),
                ('productDetailImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('imageDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('productID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.tblproducts')),
            ],
        ),
        migrations.CreateModel(
            name='tblSubFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subFooterName', models.CharField(max_length=200, null=True)),
                ('subFooterURL', models.CharField(max_length=200, null=True)),
                ('footerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.tblfooter')),
            ],
        ),
        migrations.CreateModel(
            name='tblSub2TopMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub2TopMenuName', models.CharField(max_length=200, null=True)),
                ('sub2TopMenuImage', models.CharField(max_length=200, null=True)),
                ('subTopMenuID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.tblsubtopmenu')),
            ],
        ),
        migrations.AddField(
            model_name='tblsubtopmenu',
            name='TopMenuID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.tbltopmenu'),
        ),
    ]
