# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class AccountPayment(models.Model):
    _inherit = "account.move"
    
    x_studio_description_1 = fields.Char(string='Descriptions')
    
    def _get_reconciled_info_JSON_values(self):
        self.ensure_one()

        reconciled_vals = []
        for partial, amount, counterpart_line in self._get_reconciled_invoices_partials():
            if counterpart_line.move_id.ref:
                reconciliation_ref = '%s (%s)' % (counterpart_line.move_id.name, counterpart_line.move_id.ref)
            else:
                reconciliation_ref = counterpart_line.move_id.name

            reconciled_vals.append({
                'name': counterpart_line.name,
                'journal_name': counterpart_line.journal_id.name,
                'cheque_number': counterpart_line.payment_id.cheque_number,
                'amount': amount,
                'currency': self.currency_id.symbol,
                'digits': [69, self.currency_id.decimal_places],
                'position': self.currency_id.position,
                'date': counterpart_line.date,
                'payment_id': counterpart_line.id,
                'partial_id': partial.id,
                'account_payment_id': counterpart_line.payment_id.id,
                'payment_method_name': counterpart_line.payment_id.payment_method_id.name if counterpart_line.journal_id.type == 'bank' else None,
                'move_id': counterpart_line.move_id.id,
                'ref': reconciliation_ref,
            })
        return reconciled_vals
