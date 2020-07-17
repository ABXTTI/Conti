# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError


class CarWorkshop(models.Model):
    _inherit = 'car.workshop'
    x_time_in = fields.Datetime(string="Vehicle In", store=True)
    x_time_out = fields.Datetime(string="Vehicle Out", store=True)
    x_seq = fields.Char(string='Doc Ref', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))


    @api.model
    def create(self, vals):
        vals['x_seq'] = self.env['ir.sequence'].next_by_code('car.workshop.sequence')
        result = super(CarWorkshop, self).create(vals)
        return result


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    x_enginecc = fields.Char(string="Engine CC", store=True)
    x_engineno = fields.Char(string="Engine No.", store=True)
    x_registrationdate = fields.Date(string="Registration Date.", store=True)
    x_paintcode = fields.Char(string="Paint Code", store=True)
    x_acceleration = fields.Char(string="Acceleration", store=True)
    x_aspiration = fields.Char(string="Aspiration.", store=True)
    x_bodystyle = fields.Char(string="Body Style", store=True)
    x_bore = fields.Char(string="Bore", store=True)
    x_consumptioncold = fields.Char(string="Consumption Cold", store=True)
    x_consumptioncombined = fields.Char(string="Consumption Combined", store=True)
    x_consumptionurban = fields.Char(string="Consumption Urban", store=True)
    x_cylinders = fields.Char(string="Cylinders", store=True)
    x_modelyear = fields.Integer(string="Model Year", store=True)
    x_driveaxel = fields.Char(string="Drive Axel", store=True)
    x_drivetype = fields.Char(string="Drive Type", store=True)
    x_enginemodelcode = fields.Integer(string="Engine Model Code", store=True)
    x_gears = fields.Integer(string="Gears", store=True)
    x_grossweight = fields.Float(string="Gross Weight", store=True)
    x_introductiontouk = fields.Date(string="Introduction to UK", store=True)
    x_kerweightmin = fields.Integer(string="Ker Weight Min", store=True)
    x_marketsegment = fields.Char(string="Market Segment", store=True)
    x_maxpowerbhp = fields.Integer(string="Max Power BHP", store=True)
    x_modelseries = fields.Char(string="Model Series", store=True)
    x_nocylinders = fields.Char(string="No. Cylinders", store=True)
    x_novalves = fields.Char(string="No. Valves", store=True)
    x_origin = fields.Char(string="Origin", store=True)
    x_topspeed = fields.Float(string="Top Speed", store=True)
    x_valvegear = fields.Char(string="Valve Gear", store=True)
    x_wheelplan = fields.Char(string="Wheel Plan", store=True)
    x_heightmm = fields.Float(string="Height(mm)", store=True)
    x_widthmm = fields.Float(string="Width(mm)", store=True)
    x_radiocode = fields.Char(string="Radio Code", store=True)
    x_motexpiry = fields.Date(string="MOT Expiry", store=True)

    from_date = fields.Date(string="Current Date ", default=fields.date.today(), store=True, readonly=True)
    # final_date=fields.Date(string="Last date")
    total_days = fields.Integer(string="Days Remaining")

    @api.onchange('from_date', 'x_registrationdate', 'x_motexpiry', 'total_days')
    def calculate_date(self):
        if self.from_date > self.x_registrationdate:
            if self.x_motexpiry > self.from_date:
                d1 = datetime.strptime(str(self.from_date), '%Y-%m-%d')
                d2 = datetime.strptime(str(self.x_motexpiry), '%Y-%m-%d')
                d3 = d2 - d1
                self.total_days = str(d3.days)
            else:
                raise ValidationError("MOT Expired")
        else:
            raise ValidationError("Wrong Registration Date")

