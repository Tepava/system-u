from odoo import models, fields, api

class pe_hr_employee_wizard(models.TransientModel):
    _inherit ='hr.departure.wizard'

    departure_reason = fields.Selection(selection_add=[('contract_end', 'Fin de contrat')])