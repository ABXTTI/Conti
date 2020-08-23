# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import RedirectWarning, ValidationError
# Constraint on Res.Partner
class ResPartner(models.Model):
    _inherit = 'res.partner'

    # constraint
    @api.constrains('mobile')
    @api.one
    def _check_number(self):
        if not self.mobile:
            raise ValidationError(_('Please Enter Mobile Number!'))
        if self.mobile[0] != "0" or self.mobile[1] != "3":
            raise ValidationError(_('Mobile Number Must Start With "03"'))
        mobile = int(self.mobile)
        if len(str(mobile)) != 10:
            raise ValidationError(_('Please Enter 11 Digits Only'))

    # constraint for unique mobile number
    _sql_constraints = [
        ('mobile_unique',
         'unique(mobile)',
         'Ops... Mobile number already exist - Partner might be already created! Plz Check...')
    ]


# Constraint on Hr.Employee
class Employee(models.Model):
    _inherit = 'hr.employee'


    # constraint
    @api.constrains('mobile_phone')
    @api.one
    def _check_number(self):
        if not self.mobile_phone:
            raise ValidationError(_('Please Enter Mobile Number!'))
        if self.mobile_phone[0] != "0" or self.mobile_phone[1] != "3":
            raise ValidationError(_('Mobile Number Must Start With "03"'))
        mobile = int(self.mobile_phone)
        if len(str(mobile)) != 10:
            raise ValidationError(_('Please Enter 11 Digits!'))

    # constraint for unique mobile numberS
    _sql_constraints = [
        ('mobile_phone_unique',
         'unique(mobile_phone)',
         'Ops... Mobile number already exist - Employee might be already created! Plz Check...')
    ]
