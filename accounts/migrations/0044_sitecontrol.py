from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_loanapplication_current_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_title', models.CharField(default='Panel System', max_length=120)),
                ('expires_at', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Site Control',
                'verbose_name_plural': 'Site Controls',
            },
        ),
    ]
