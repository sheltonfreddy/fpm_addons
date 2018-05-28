from odoo import api, fields, models, _

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def invoice_print_without_pay(self):
        """ Print the invoice without payment
        """
        self.ensure_one()
        return self.env.ref('account.account_invoices_without_payment').report_action(self)