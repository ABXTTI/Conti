from odoo import models, fields, api, _
class AccountInvoice(models.Model):
    _inherit = ['account.invoice']

    def get_int(self):
        for rec in self:
            if type(rec.x_total) == float:
                rec.x_total = round(rec.x_total)
                rec.amount_total = round(rec.amount_total)
