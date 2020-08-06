# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError

class AccountInvoice(models.Model):
     _inherit = ['account.invoice']

     job_no=fields.Char(string="Job Number")
     relation=fields.Many2one(string="Relation", related='x_ref.vehicle_id')
     x_ref=fields.Many2one('car.workshop', compute='get_origin')
     @api.multi
     def get_origin(self):
         for rec in self:
             res=rec.env['car.workshop'].search([('id','=',rec.job_no)])
             rec.x_ref=res

class AccountInvoice(models.Model):
    _inherit = 'account.invoice.line'
    x_tcost = fields.Text(string="Cost", readonly=True)

class CarWorkshop(models.Model):
    _inherit = 'car.workshop'
    amount_totals = fields.Float(string="Total Cost", readonly=True, compute="amount_total2")

    @api.depends('planned_works.x_com', 'materials_used.price', 'materials_used.amount')
    def amount_total2(self):
        for records in self:
            for hour in records:
                amount_totall = 0.0
                for line in hour.planned_works:
                    amount_totall += line.x_com
                for line2 in hour.materials_used:
                    amount_totall += line2.x_cost2 * line2.amount
                records.amount_totals = amount_totall

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    x_total = fields.Float(string="Total Cost", readonly=True)

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    job_no = fields.Integer(string="Job Number")
    x_vehicle = fields.Many2one(string="Vehicle", related='x_ref.vehicle_id')
    x_ref = fields.Many2one('car.workshop', compute='get_vehicle')
    # x_vehicle = fields.Many2one(string="Vehicle")
    x_job_ref= fields.Char(string="Job Ref", readonly=True)

    @api.multi
    def get_vehicle(self):
        for rec in self:
            res = rec.env['car.workshop'].search([('x_seq', '=', rec.x_job_ref)])
            rec.x_ref = res

class StockMove(models.Model):
    _inherit = 'stock.move'
    x_vehicle = fields.Many2one(string="Vehicle Ref", related='picking_id.x_vehicle', readonly=True,)
    x_job_ref= fields.Char(string="Job Ref",related='picking_id.x_job_ref', readonly=True)









