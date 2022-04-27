from odoo import models, fields, api

class pe_hr_employee(models.Model):
    _inherit = 'hr.employee'
    
    departure_reason = fields.Selection(selection_add=[('contract_end', 'Fin de contrat')])