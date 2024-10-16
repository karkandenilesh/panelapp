import pandas as pd
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PanelInformation
from .serializers import PanelInformationSerializer

@api_view(['POST'])
def create_panel_information(request):
    # Deserialize the incoming JSON data into the PanelInformation model
    serializer = PanelInformationSerializer(data=request.data)
    
    # Check if the provided data is valid
    if serializer.is_valid():
        serializer.save()  # Save the data to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created object in the response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if the data is not valid



@api_view(['GET'])
def get_panel_information(request, panel_id):
    try:
        panel_info = PanelInformation.objects.get(panel_id=panel_id)  # Fetch record by panel_id
    except PanelInformation.DoesNotExist:
        return Response({'error': 'Panel not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PanelInformationSerializer(panel_info)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_panel_data(request):
    print("***")
    # Fetch all PanelInformation objects
    panels = PanelInformation.objects.all()
    print(panels)

    # Serialize the data
    serializer = PanelInformationSerializer(panels, many=True)

    # Return the serialized data
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def upload_excel(request):
    if 'file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

    file = request.FILES['file']

    # Check if the file is an Excel file
    if not file.name.endswith('.xlsx'):
        return Response({'error': 'File type not supported. Please upload an Excel (.xlsx) file.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file)

        # Replace all NaN values with None (which becomes NULL in the database)
        df = df.where(pd.notnull(df), None)

        # Iterate through each row and save it to the database
        for index, row in df.iterrows():
            data = {
                'client_name': row['Client Name'],
                'project_name': row['ProjectName'],
                'client_circle': row['Client Circle'],
                'state': row['State'],
                'city': row['City'],
                'pincode': row['Pincode'],
                'address': row['Address'],
                'branch_name': row['Branch Name'],
                'panel_ip': row['Panel IP'],
                'panel_location': row['Panel Location'],
                'panel_type': row['Panel Type'],
                'panel_id': row['Panel ID'],
                'panel_port': row['Panel Port'],
                'panel_manufacturer_id': row['Panel Manufacturer ID'],
                'panel_manufacturer': row['Panel Manufacturer'],
                'panel_model': row['Panel Model'],
                'panel_current_version': row['Panel Current Version'],
                'solid_site_id': row['SolId / SiteID'],
                'mdn_numbers': row['MDN Numbers'],
                'atm_1_id': row['ATM 1 ID'],
                'atm_2_id': row['ATM 2 ID'],
                'atm_3_id': row['ATM 3 ID'],
                'atm_4_id': row['ATM 4 ID'],
                'atm_5_id': row['ATM 5 ID'],
                'cra_company': row['CRA Company'],
                'msp_company': row['MSP Company'],
                'hk_company': row['HK Company'],
                'installation_vendor': row['Installation Vendor'],
                'project_coordinator': row['Project Co-ordinator'],
                'project_lead': row['Project Lead'],
                'project_manager': row['Project Manager'],
                'securens_territory_name': row['Securens Territory Name'],
                'territory_manager_name': row['Territory Manager Name'],
                'antenna': row['Antenna'],
                'subscription': row['Subscription'],
                'dvr_user_id': row['DVR User ID'],
                'dvr_user_password': row['DVR User Password'],
                'dvr_port': row['DVR Port'],
                'dvr_type': row['DVR Type'],
                'user_circle': row['User Circle'],
                'category': row['Category'],
                'panel_status': row['Panel Status'],
                'em': row['EM'],
                'pm': row['PM'],
                'latitude': row['Latitude'],
                'longitude': row['Longitude'],
                'services': row['Services'],
                'sim_1_no': row['Sim 1 No'],
                'sim_2_no': row['Sim 2 No'],
                'sim_3_no': row['Sim 3 No'],
                'dial_100_send_sms': row['Dial 100 Send SMS'],
                'dial_100_sms_string': row['Dial 100 SMS String'],
            }

            # Create an instance of the PanelInformation model and save it
            serializer = PanelInformationSerializer(data=data)

            if serializer.is_valid():
                print("444")
                try:
                    serializer.save()  # Try saving to the database
                    print("555")
                except Exception as e:
                    return Response({'error': f"Error saving row {index + 1}: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # If the row contains invalid data, return the error message
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Data uploaded successfully'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



