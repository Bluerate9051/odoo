# -*- coding: utf-8 -*-

# import pytz
# from datetime import datetime
# from unittest.mock import patch

from odoo import fields
from odoo.tests import new_test_user
from odoo.tests.common import TransactionCase


class TestHrAttendanceLocation(TransactionCase):
    """Test for presence validity"""

    def setUp(self):
        super(TestHrAttendanceLocation, self).setUp()
        self.user = new_test_user(self.env, login='user', groups='base.group_user')
        self.hr_attendance_obj = self.env['hr.attendance']
        self.test_employee = self.env['hr.employee'].create({
            'name': "Employee A",
            'user_id': self.user.id,
        })

    def test_employee_attendance_location(self):
        # Make sure location attendance of the employee equal to current location
        current_lat, current_lng = self.test_employee.get_current_lat_lng()
        self.test_employee._attendance_action_change()
        # assert self.test_employee.attendance_state == 'checked_in'
        assert self.test_employee.attendance_state == 'checked_in'
        employee_attendance = self.hr_attendance_obj.search([
            ('employee_id', '=', self.test_employee.id)])
        # assert employee_attendance[0].check_in_lat == current_lat
        self.assertEqual(
            round(employee_attendance[0].check_in_lat,1), float(current_lat))
        print("Successful!")
        # assert employee_attendance[0].check_in_lng == current_lat
        self.assertEqual(
            round(employee_attendance[0].check_in_lng,1), float(current_lng))
        print("Successful!")
        current_lat, current_lng = self.test_employee.get_current_lat_lng()
        self.test_employee._attendance_action_change()
        # assert self.test_employee.attendance_state == 'checked_out'
        assert self.test_employee.attendance_state == 'checked_out'
        # assert employee_attendance[0].check_out_lat == current_lat
        self.assertEqual(
            round(employee_attendance[0].check_out_lat,1), float(current_lat))
        print("Successful!")
        # assert employee_attendance[0].check_out_lng == current_lng
        self.assertEqual(
            round(employee_attendance[0].check_out_lng,1), float(current_lng))
        print("Successful!")