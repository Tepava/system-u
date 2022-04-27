# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"
    
    cheque_number = fields.Char(string='Numéro du chèque')

#     ID des cheques 9 e
#     action_create_payments = action de création d'un paiement
#     _create_payment_vals_from_wizard = création d'un paiement à partir du wizard

    def _create_payment_vals_from_wizard(self):
        payment_vals = {
            'date': self.payment_date,
            'amount': self.amount,
            'payment_type': self.payment_type,
            'partner_type': self.partner_type,
            'ref': self.communication,
            'journal_id': self.journal_id.id,
            #Ajout du numéros de chèque
            'cheque_number': self.cheque_number,
            'currency_id': self.currency_id.id,
            'partner_id': self.partner_id.id,
            'partner_bank_id': self.partner_bank_id.id,
            'payment_method_id': self.payment_method_id.id,
            'destination_account_id': self.line_ids[0].account_id.id
        }

        if not self.currency_id.is_zero(self.payment_difference) and self.payment_difference_handling == 'reconcile':
            payment_vals['write_off_line_vals'] = {
                'name': self.writeoff_label,
                'amount': self.payment_difference,
                'account_id': self.writeoff_account_id.id,
            }
        return payment_vals