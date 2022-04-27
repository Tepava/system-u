# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class AccountPaymentFix(models.Model):
    _inherit = "account.payment"
    
    x_studio_description_1 = fields.Char(string='Paiement Description')

class ReleveBancaireLigneFix(models.Model):
    _inherit = "account.bank.statement.line"
    
    x_studio_description_1 = fields.Char(string='Releve Bancaire Ligne Description')