# Generated by Django 4.2.7 on 2023-12-10 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polka', '0011_remove_cart_books'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='books2',
            new_name='books',
        ),
    ]