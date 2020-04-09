# -*- coding: utf-8 -*-

import time

from odoo.tests.common import TransactionCase


class TestHrAttendanceGeofence(TransactionCase):
    """Tests for attendance geofence area"""

    def setUp(self):
        super(TestHrAttendanceGeofence, self).setUp()
        self.attendance_geofence = self.env['hr.attendance.area'].create({
            'shape_name': 'Work Area',
            'attendance_ok': True,
            'shape_description': 'Work Area Geofence.',
        })

    def test_attendance_geofence_only_one(self):
        # Make sure geofence area of attendance is created only once
        with self.assertRaises(Exception):
            self.my_attend = self.env['hr.attendance.area'].create({
               'shape_name': 'Remote Work Area',
                'attendance_ok': True,
                'shape_description': 'Remote Work Area Geofence.',
            })