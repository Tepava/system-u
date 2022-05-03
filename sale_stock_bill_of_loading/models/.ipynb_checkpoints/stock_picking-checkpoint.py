# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    lst_price = fields.Float(compute="get_lst_price", inverse="set_lst_price", store=True)

    @api.depends('sale_line_id')
    def get_lst_price(self):
        for this in self:
            product = this.sale_line_id.product_id
            if product:
                # Check if is a manufactured product
                if product.bom_ids:
                    this.lst_price = this.product_id.lst_price
                else:
                    this.lst_price = this.sale_line_id.price_unit

    def set_lst_price(self):
        pass
