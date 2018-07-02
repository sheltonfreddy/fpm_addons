# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order', 'barcodes.barcode_events_mixin']

    def _add_product(self, product, weight, qty=1.0):
        order_line = self.order_line.filtered(lambda r: r.product_id.id == product.id)
        if order_line:
            order_line.weights += ',' + weight
            order_line.product_uom_change()
            order_line.onchange_weights()
        else:
            vals = {
                'product_id': product.id,
                'product_uom': product.uom_id.id,
                #'product_uom_qty': 1,
                'state': 'draft',
                'weights': weight
                }
            order_line = self.order_line.new(vals)
            order_line.product_id_change()
            order_line.product_uom_change()
            order_line.onchange_weights()
            self.order_line += order_line


    def on_barcode_scanned(self, barcode):
        if barcode:
            barcode_weight = barcode.split()
            if len(barcode_weight) != 2:
                raise UserError(_('Product code and Weight not Captured! Please try again!!'))
        if self.state != 'draft':
            return
        product = self.env['product.product'].search([('barcode', '=', barcode_weight[0])])
        if product:
            weight = barcode_weight[1]
            self._add_product(product,weight)

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    last_price = fields.Float('Last Price', compute="_compute_last_price")

    @api.multi
    def _compute_last_price(self):
        """ Print the invoice without payment
        """
        for line in self:
            lines = self.env['sale.order.line'].search([('order_partner_id', '=', line.order_partner_id.id),
                                                        ('product_id', '=', line.product_id.id),
                                                        ('order_id', '!=', line.order_id.id),
                                                        ('order_id.state', 'not in', ['draft','cancel'])],
                                                       order='create_date DESC', limit=1)
            if not lines:
                line.last_price=0
                break
            line.last_price = lines and lines.price_unit or 0

