# -*- coding: utf-8 -*-
{
    'name': 'Attendance Geofence Area Status',
    'version': '13.0.1.0.1',
    'author': 'Tibyan Hussien',
    'support': 'tib9051@gmail.com',
    'category': 'HR',
    'description': """
Status of Attendance Area
========================
This module extends web_google_maps_drawing that determines the status of attendance drawing geofence area. The main functionalities are:

1. gets current location and compares that with attendance geofence area in order to calculate the status of manual attendance employee current location whether it is inside or outside geofence area
2. sends notification of calculated state to login employee
3. Geofence Map can be viewed in any selected language
""",
    'depends': [
        'web_google_maps_drawing',
        'hr_attendance',
        'mail'
    ],
    'website': '',
    'data': [
        'security/ir.model.access.csv',
        'views/hr_attendance_view.xml',
        'views/hr_attendance_area.xml',
    ],
    "external_dependencies": {"python" : ["shapely"]},
    'installable': True
}