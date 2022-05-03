# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class AccountPayment(models.Model):
    _inherit = "account.move"
    
    def _get_reconciled_vals(self):
        # OVERRIDE
        # Ajout du numéros de chèque
        reconciled_vals = super()._get_reconciled_vals()
        reconciled_vals['cheque_number'] = counterpart_line.payment_id.cheque_number
        return reconciled_vals