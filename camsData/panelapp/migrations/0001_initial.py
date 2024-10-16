# Generated by Django 5.1.2 on 2024-10-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PanelInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=255, null=True)),
                ('project_name', models.CharField(blank=True, max_length=255, null=True)),
                ('client_circle', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=255, null=True)),
                ('panel_ip', models.CharField(blank=True, max_length=255, null=True)),
                ('panel_location', models.TextField(blank=True, null=True)),
                ('panel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('panel_id', models.CharField(max_length=100)),
                ('panel_port', models.IntegerField(blank=True, null=True)),
                ('panel_manufacturer_id', models.CharField(blank=True, max_length=100, null=True)),
                ('panel_manufacturer', models.CharField(blank=True, max_length=255, null=True)),
                ('panel_model', models.CharField(blank=True, max_length=255, null=True)),
                ('panel_current_version', models.CharField(blank=True, max_length=50, null=True)),
                ('sol_site_id', models.CharField(blank=True, max_length=100, null=True)),
                ('mdn_numbers', models.CharField(blank=True, max_length=20, null=True)),
                ('atm_1_id', models.CharField(blank=True, max_length=100, null=True)),
                ('atm_2_id', models.CharField(blank=True, max_length=100, null=True)),
                ('atm_3_id', models.CharField(blank=True, max_length=100, null=True)),
                ('atm_4_id', models.CharField(blank=True, max_length=100, null=True)),
                ('atm_5_id', models.CharField(blank=True, max_length=100, null=True)),
                ('cra_company', models.CharField(blank=True, max_length=255, null=True)),
                ('msp_company', models.CharField(blank=True, max_length=255, null=True)),
                ('hk_company', models.CharField(blank=True, max_length=255, null=True)),
                ('installation_vendor', models.CharField(blank=True, max_length=255, null=True)),
                ('project_coordinator', models.CharField(blank=True, max_length=255, null=True)),
                ('project_lead', models.CharField(blank=True, max_length=255, null=True)),
                ('project_manager', models.CharField(blank=True, max_length=255, null=True)),
                ('securens_territory_name', models.CharField(blank=True, max_length=255, null=True)),
                ('territory_manager_name', models.CharField(blank=True, max_length=255, null=True)),
                ('antenna', models.CharField(blank=True, max_length=100, null=True)),
                ('subscription', models.CharField(blank=True, max_length=100, null=True)),
                ('dvr_user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('dvr_user_password', models.CharField(blank=True, max_length=255, null=True)),
                ('dvr_port', models.CharField(blank=True, max_length=255, null=True)),
                ('dvr_type', models.CharField(blank=True, max_length=255, null=True)),
                ('user_circle', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('panel_status', models.CharField(blank=True, max_length=50, null=True)),
                ('em', models.CharField(blank=True, max_length=50, null=True)),
                ('pm', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('services', models.CharField(blank=True, max_length=255, null=True)),
                ('sim_1_no', models.CharField(blank=True, max_length=50, null=True)),
                ('sim_2_no', models.CharField(blank=True, max_length=50, null=True)),
                ('sim_3_no', models.CharField(blank=True, max_length=50, null=True)),
                ('dial_100_send_sms', models.CharField(blank=True, max_length=100, null=True)),
                ('dial_100_sms_string', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
