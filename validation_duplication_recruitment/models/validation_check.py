# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import RedirectWarning, ValidationError
# Constraint on Res.Partner
class Applicant(models.Model):
    _inherit = 'hr.applicant'

    partner_id = fields.Many2one('hr.applicant', string="Create Partner", readonly=True)


    # constraint
    @api.constrains('partner_mobile')
    @api.one
    def _check_number(self):
        vals = self.env['hr.applicant'].search([('partner_mobile', '=', self.partner_mobile)])
        print len(vals)
        if len(vals)>1:
            raise ValidationError(_('Record Already Exist!'))
        if not self.partner_mobile:
            raise ValidationError(_('Please Enter Mobile Number!'))
        if self.partner_mobile[0] != "0" or self.partner_mobile[1] != "3":
            raise ValidationError(_('Mobile Number Must Start With "03"'))
        mobile = int(self.partner_mobile)
        if len(str(mobile)) != 10:
            raise ValidationError(_('Please Enter 11 Digits Only'))
