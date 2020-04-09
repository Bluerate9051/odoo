# -*- encoding: utf-8 -*-
from odoo import fields, models,api,_
import math
from odoo.exceptions import UserError, ValidationError
import requests

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def get_current_lat_lng(self):
        """Get current geolocationIP latitude and longitude.
           ===================Note==========================
           Latitude and longitude may not accurate because of 
           not being able to use Google Maps packages cause 
           of sanctions on Sudan.
           """
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        current_ip = ip_request.json()['ip']
        geolocation_req = requests.get('https://get.geojs.io/v1/ip/geo/' + current_ip + '.json')
        geolocation_dict = geolocation_req.json()
        return [geolocation_dict['latitude'],geolocation_dict['longitude']]

    def attendance_manual(self, next_action, entered_pin=False,
                          location=False):
        res = super(HrEmployee, self.with_context(
            attendance_location=location)).attendance_manual(
            next_action, entered_pin)
        return res

    def _attendance_action_change(self):
        res = super()._attendance_action_change()
        self.ensure_one()
        attendance_geofence = self.env['hr.attendance.area'].search([('attendance_ok','=',True)])
        location = self.get_current_lat_lng()
        state = attendance_geofence._compute_geofence_state(float(location[0]),float(location[1]))
        if location and attendance_geofence:
            if self.attendance_state == 'checked_in':
                res.write({
                    'check_in_lat': float(location[0]),
                    'check_in_lng': float(location[1]),
                    'geofence_id': attendance_geofence[0].id,
                    'check_in_geo_state': state
                })
                if attendance_geofence[0].notify_user:
                    self.message_post(type="email",body=('%s is %s geofence area.') % (self.name,res['check_in_geo_state']))
            else:
                res.write({
                    'check_out_lat': float(location[0]),
                    'check_out_lng': float(location[1]),
                    'check_out_geo_state': state
                })
                if attendance_geofence[0].notify_user:
                    self.message_post(type="email",body=('%s is %s geofence area.') % (self.name,res['check_out_geo_state']))
        else:
            raise ValidationError(_("Please Attendance Geofence should be set before Check-in/out"))
        return res
