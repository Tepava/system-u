# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class AccountPayment(models.Model):
    _inherit = "account.payment"
    
    cheque_number = fields.Char(string='Numéro du chèque')
    account_move_link = fields.Many2one(string='Liens vers Invoice', comodel_name='account.move')
    