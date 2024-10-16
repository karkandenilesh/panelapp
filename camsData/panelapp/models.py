from django.db import models

class PanelInformation(models.Model):
    client_name = models.CharField(max_length=255, blank=True, null=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    client_circle = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    panel_ip = models.CharField(max_length=255, blank=True, null=True)
    panel_location = models.TextField(blank=True, null=True)
    panel_type = models.CharField(max_length=100, blank=True, null=True)
    panel_id = models.CharField(max_length=100)
    panel_port = models.CharField(max_length=100, blank=True, null=True)
    panel_manufacturer_id = models.CharField(max_length=100, blank=True, null=True)
    panel_manufacturer = models.CharField(max_length=255, blank=True, null=True)
    panel_model = models.CharField(max_length=255, blank=True, null=True)
    panel_current_version = models.CharField(max_length=50, blank=True, null=True)
    sol_site_id = models.CharField(max_length=100, null=True, blank=True)
    mdn_numbers = models.CharField(max_length=20, blank=True, null=True)
    
    # ATM IDs
    atm_1_id = models.CharField(max_length=100, blank=True, null=True)
    atm_2_id = models.CharField(max_length=100, blank=True, null=True)
    atm_3_id = models.CharField(max_length=100, blank=True, null=True)
    atm_4_id = models.CharField(max_length=100, blank=True, null=True)
    atm_5_id = models.CharField(max_length=100, blank=True, null=True)
    
    cra_company = models.CharField(max_length=255, blank=True, null=True)
    msp_company = models.CharField(max_length=255, blank=True, null=True)
    hk_company = models.CharField(max_length=255, blank=True, null=True)
    installation_vendor = models.CharField(max_length=255, blank=True, null=True)
    project_coordinator = models.CharField(max_length=255, blank=True, null=True)
    project_lead = models.CharField(max_length=255, blank=True, null=True)
    project_manager = models.CharField(max_length=255, blank=True, null=True)
    securens_territory_name = models.CharField(max_length=255, blank=True, null=True)
    territory_manager_name = models.CharField(max_length=255, blank=True, null=True)
    antenna = models.CharField(max_length=100, blank=True, null=True)
    subscription = models.CharField(max_length=100, blank=True, null=True)
    
    # DVR details
    dvr_user_id = models.CharField(max_length=255, blank=True, null=True)
    dvr_user_password = models.CharField(max_length=255, blank=True, null=True)
    dvr_port = models.CharField(max_length=255, blank=True, null=True)
    dvr_type = models.CharField(max_length=255, blank=True, null=True)
    
    # Additional details
    user_circle = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    panel_status = models.CharField(max_length=50, blank=True, null=True)
    em = models.CharField(max_length=50, blank=True, null=True)
    pm = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    
    # Services and SIM details
    services = models.CharField(max_length=255, blank=True, null=True)
    sim_1_no = models.CharField(max_length=50, null=True, blank=True)
    sim_2_no = models.CharField(max_length=50, null=True, blank=True)
    sim_3_no = models.CharField(max_length=50, null=True, blank=True)
    
    # Dial 100 and SMS information
    dial_100_send_sms = models.CharField(max_length=100, blank=True, null=True)
    dial_100_sms_string = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.client_name} - {self.project_name} - {self.panel_id}"


