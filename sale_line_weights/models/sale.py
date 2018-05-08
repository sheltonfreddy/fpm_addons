# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    weights = fields.Text('Weights')
    total_weight = fields.Float('Total Weight')

    @api.onchange('weights')
    def onchange_weights(self):
        weight=0
        if self.weights:
            weight_list = self.weights.split(',')
            for elem in weight_list:
                weight += float(elem)
            self.total_weight = weight
            if weight > 0:
                self.product_uom_qty = weight

