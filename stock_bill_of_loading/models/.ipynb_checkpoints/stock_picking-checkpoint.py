# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    move_ids_bill_of_loading = fields.One2many(comodel_name='stock.move', inverse_name='picking_id', )
    total_weight = fields.Float(compute='_compute_total_weight_and_volumd', string='Total poids')
    total_volume = fields.Float(compute='_compute_total_weight_and_volumd', string='Total volume')
    valuation = fields.Float(compute='_compute_total_weight_and_volumd', string='Valeur Total')

    def _compute_total_weight_and_volumd(self):
        for this in self:
            this.total_weight = 0
            this.total_volume = 0
            this.valuation = 0
            for move in this.move_ids_bill_of_loading:
                this.total_volume += move.total_volume
                this.total_weight += move.total_weight
                this.valuation += move.valuation


class StockMove(models.Model):
    _inherit = 'stock.move'

    weight = fields.Float(related='product_id.weight', string='Poids', digits='Stock Weight')
    total_weight = fields.Float(compute='_compute_total_weight_and_volumd', string='Sous total poids')

    volume = fields.Float(related='product_id.volume', string='Volume', digits='Volume')
    total_volume = fields.Float(compute='_compute_total_weight_and_volumd', string='Sous total volume')

    lst_price = fields.Float(string='Valeur unitaire', readonly=True, states={'draft': [('readonly', False)]})
    valuation = fields.Float(compute='_compute_total_weight_and_volumd', string='Valeur')

    @api.onchange('product_id')
    def update_lst_price_onchange_product_id(self):
        if self.product_id:
            self.lst_price = self.product_id.lst_price

    def _compute_total_weight_and_volumd(self):
        for this in self:
            this.total_weight = this.weight * this.quantity_done
            this.total_volume = this.volume * this.quantity_done
            this.valuation = this.product_qty * this.lst_price
