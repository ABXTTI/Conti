# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError

class CarWorkshop(models.Model):
    _inherit = 'car.workshop'


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

class PlannedWork (models.Model):
    _inherit = 'planned.work'

    @api.depends('planned_work')
    def get_cost(self):
        for self in self:
            self.x_cost = self.planned_work.standard_price

    @api.depends('time_spent','duration')
    def get_multiply2(self):
        for rec in self:
            rec.x_com = rec.time_spent * rec.x_cost
            rec.x_com1 = rec.duration * rec.x_cost


    x_cost = fields.Float(string="Internal Cost", compute="get_cost", store=True, readonly=True)
    x_com = fields.Float(string="Total Cost", compute="get_multiply2", store=True, readonly=True)
    x_com1 = fields.Float(string="Total Price", compute="get_multiply2", store=True, readonly=True)

    # x_cost = fields.Float(string="Internal Cost")
    # x_com=fields.Float(string="Hourly Cost", compute="get_multiply")
    # # x_cost1 = fields.Float(string="Internal Cost", readonly=True)
    # x_com1 = fields.Float(string="Hourly Cost", compute="get_multiply")
    #
    # @api.onchange('planned_work')
    # def get_cost(self):
    #     self.x_cost = self.planned_work.standard_price
    #
    # @api.multi
    # def get_multiply(self):
    #     for rec in self:
    #         rec.x_com1=rec.duration*rec.x_cost
    #         rec.x_com=rec.time_spent*rec.x_cost

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

    @api.depends('material')
    def get_cost2(self):
        for self in self:
            self.x_cost2 = self.material.standard_price

    @api.depends('amount')
    def get_multiply2(self):
         for rec in self:
             rec.x_com2 = rec.amount * rec.x_cost2
             rec.x_com3 = rec.price * rec.amount

    x_cost2 = fields.Float(string="Internal Cost", compute="get_cost2", store=True, readonly=True)
    x_com2 = fields.Float(string="Total Cost", compute="get_multiply2", store=True, readonly=True)
    x_com3 = fields.Float(string="Total Price", compute="get_multiply2", store=True, readonly=True)

    # @api.onchange('material')
    # def get_cost2(self):
    #     self.x_cost2 = self.material.standard_price

    # @api.multi
    # def get_multiply2(self):
    #     for rec in self:
    #         rec.x_com2 = rec.amount * rec.x_cost2
    #         rec.x_com3 = rec.price * rec.amount

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
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    job_ref = fields.Many2one('car.workshop','x_seq', string="Job Reference", required=True)







