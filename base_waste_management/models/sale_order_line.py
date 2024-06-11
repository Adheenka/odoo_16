

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    waste_category = fields.Many2one(
        'product.category',
        string='Waste Category',
        related='order_id.waste_category_id',
        store=True
    )
