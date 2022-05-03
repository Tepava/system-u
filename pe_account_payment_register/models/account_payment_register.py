# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"
    
    cheque_number = fields.Char(string='Numéro du chèque')

#     ID des cheques 9 e
#     action_create_payments = action de création d'un paiement
#     _create_payment_vals_from_wizard = création d'un paiement à partir du wizard
    
    def _create_payment_vals_from_wizard(self):
        # OVERRIDE
        # Ajout du numéros de chèque
        payment_vals = super()._create_payment_vals_from_wizard()
        payment_vals['cheque_number'] = self.cheque_number
        return payment_vals