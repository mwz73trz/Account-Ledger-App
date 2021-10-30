# Generated by Django 3.2.8 on 2021-10-30 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=10)),
                ('check_number', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.CharField(max_length=254)),
                ('deposit_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('withdrawal_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ledgers', to='account_ledger_app.account')),
            ],
        ),
    ]
