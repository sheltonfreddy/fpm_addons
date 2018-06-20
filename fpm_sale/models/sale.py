# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

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

