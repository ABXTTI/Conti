from odoo import models, fields, api, _
# class ResCompany(models.Model):
#     _inherit = 'res.company'
#     round_invoice=fields.Boolean(string='Rounding Of Invoice')

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'
    x_discount_amount = fields.Float(string="Discount Amount")

    @api.one
    @api.depends('price_unit', 'discount', 'x_discount_amount', 'invoice_line_tax_ids', 'quantity',
                 'product_id', 'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id',
                 'invoice_id.date_invoice', 'invoice_id.date')
    def _compute_price(self):
        currency = self.invoice_id and self.invoice_id.currency_id or None
        if self.x_discount_amount:
            self.discount = self.x_discount_amount/self.price_unit * 100
            price = self.price_unit - self.x_discount_amount
        else:
            if self.discount:
                self.x_discount_amount = self.price_unit * self.discount/100
            elif self.discount and self.x_discount_amount:
                self.x_discount_amount = self.price_unit * self.discount/100
            price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
        taxes = False
        if self.invoice_line_tax_ids:
            taxes = self.invoice_line_tax_ids.compute_all(price, currency, self.quantity, product=self.product_id,
                                                          partner=self.invoice_id.partner_id)
        self.price_subtotal = price_subtotal_signed = taxes['total_excluded'] if taxes else self.quantity * price
        if self.invoice_id.currency_id and self.invoice_id.company_id and self.invoice_id.currency_id != self.invoice_id.company_id.currency_id:
            price_subtotal_signed = self.invoice_id.currency_id.with_context(
                date=self.invoice_id._get_currency_rate_date()).compute(price_subtotal_signed,
                                                                        self.invoice_id.company_id.currency_id)
        sign = self.invoice_id.type in ['in_refund', 'out_refund'] and -1 or 1
        self.price_subtotal_signed = price_subtotal_signed * sign


    # @api.one
    # @api.depends('price_unit')
    # def get_int(self):
    #         if self.product_id.company_id.round_invoice:
    #             self.price_subtotal=round(self.quantity*self.price_unit)
    #         else:
    #             self.price_subtotal = self.quantity * self.price_unit
    #
    # price_subtotal=fields.Float(compute='get_int', store=True)
    # @api.one
    # @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'currency_id', 'company_id', 'date_invoice', 'type')
    # def _compute_amount(self):
    #     round_curr = self.currency_id.round
    #     self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line_ids)
    #     self.amount_tax = sum(round_curr(line.amount) for line in self.tax_line_ids)
    #
    #     self.amount_total = self.amount_untaxed + self.amount_tax
    #     amount_total_company_signed = self.amount_total
    #     amount_untaxed_signed = self.amount_untaxed
    #     if self.currency_id and self.company_id and self.currency_id != self.company_id.currency_id:
    #         currency_id = self.currency_id.with_context(date=self.date_invoice)
    #         amount_total_company_signed = currency_id.compute(self.amount_total, self.company_id.currency_id)
    #         amount_untaxed_signed = currency_id.compute(self.amount_untaxed, self.company_id.currency_id)
    #     sign = self.type in ['in_refund', 'out_refund'] and -1 or 1
    #     self.amount_total_company_signed = amount_total_company_signed * sign
    #     self.amount_total_signed = self.amount_total * sign
    #     self.amount_untaxed_signed = amount_untaxed_signed * sign



