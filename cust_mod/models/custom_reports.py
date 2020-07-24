# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError

class AccountInvoice(models.Model):
     _inherit = 'account.invoice'
     relation=fields.Many2one(string="Relation", related='x_ref.vehicle_id')
     x_ref=fields.Many2one('car.workshop', compute='get_origin')
     @api.multi
     def get_origin(self):
         for rec in self:
             res=rec.env['car.workshop'].search([('name','=',rec.origin)])
             rec.x_ref=res



class CarWorkshop(models.Model):
    _inherit = 'car.workshop'


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

class PlannedWork (models.Model):
    _inherit = 'planned.work'

    x_cost = fields.Float(string="Internal Cost")
    x_com=fields.Float(string="Hourly Cost", compute="get_multiply")
    # x_cost1 = fields.Float(string="Internal Cost", readonly=True)
    x_com1 = fields.Float(string="Hourly Cost", compute="get_multiply")
    @api.onchange('planned_work')
    def get_cost(self):
        self.x_cost = self.planned_work.standard_price

    @api.multi
    def get_multiply(self):
        for rec in self:
            rec.x_com1=rec.duration*rec.x_cost
            rec.x_com=rec.time_spent*rec.x_cost

    # @api.onchange('works_done')
    # def get_cost1(self):
    #     self.x_cost1 = self.planned_work.standard_price

    # @api.multi
    # def get_multiply1(self):
    #     for rec in self:
    #         rec.x_com1= rec.time_spent * rec.x_cost1


    # @api.multi
    # def get_hour_x_cost(self):
    #     for self in self:
    #         self.x_com=self.time_spent*self.x_cost
    #         return self.x_com

class MaterialUsed (models.Model):
    _inherit = 'material.used'
    x_cost2 = fields.Float(string="Internal Cost", readonly=True)
    x_com2 = fields.Float(string="Total Cost", compute="get_multiply2")
    x_com3 = fields.Float(string="Total Price", compute="get_multiply2")

    @api.onchange('material')
    def get_cost2(self):
        self.x_cost2 = self.material.standard_price
        print self.x_cost2

    @api.multi
    def get_multiply2(self):
        for rec in self:
            rec.x_com2= rec.amount * rec.x_cost2
            rec.x_com3=rec.price*rec.amount

# class CarWorkshop (models.Model):
#     _name = 'car.workshop'
#     x_cost1 = fields.Float(string="Internal Cost", readonly=True)
#     x_com1 = fields.Float(string="Hourly Cost", compute="get_multiply")
#
#     @api.onchange('works_done')
#     def get_cost(self):
#         self.x_cost1 = self.works_done.standard_price
#
#     @api.multi
#     def get_multiply(self):
#         for rec in self:
#             rec.x_com1 = rec.duration * rec.x_cost







