# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError

class AccountInvoice(models.Model):
     _inherit = 'account.invoice'
     job_no=fields.Char(string="Job Number")
     relation=fields.Many2one(string="Relation", related='x_ref.vehicle_id')
     x_ref=fields.Many2one('car.workshop', compute='get_origin')
     @api.multi
     def get_origin(self):
         for rec in self:
             res=rec.env['car.workshop'].search([('id','=',rec.job_no)])
             rec.x_ref=res










