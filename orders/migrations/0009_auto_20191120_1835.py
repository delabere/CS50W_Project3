# Generated by Django 2.2.7 on 2019-11-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_pizza_pizza_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='pizzatopping',
            name='pizzas',
        ),
        migrations.RemoveField(
            model_name='subtopping',
            name='subs',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='pizza', to='orders.PizzaTopping'),
        ),
        migrations.AddField(
            model_name='sub',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='sub', to='orders.PizzaTopping'),
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='pizza_type',
        ),
        migrations.RemoveField(
            model_name='sub',
            name='sub_type',
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizza_type',
            field=models.ManyToManyField(blank=True, related_name='pizza', to='orders.PizzaType'),
        ),
        migrations.AddField(
            model_name='sub',
            name='sub_type',
            field=models.ManyToManyField(blank=True, related_name='sub', to='orders.SubType'),
        ),
    ]
