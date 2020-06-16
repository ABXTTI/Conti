# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime

class CarWorkshop(models.Model):
    _inherit = 'car.workshop'
    x_time_in = fields.Datetime(string="Vehicle In", store=True)
    x_time_out = fields.Datetime(string = "Vehicle Out", store=True)
