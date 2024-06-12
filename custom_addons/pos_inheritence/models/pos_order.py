from odoo import models, fields, api


class PosOrder(models.Model):
    _inherit = 'pos.order'


    delivery_country = fields.Many2one('res.country', string='Delivery Country')
    delivery_type = fields.Selection([
        ('domestic', 'Domestic'),
        ('international', 'International'),
    ], string='Delivery Type')
    expected_delivery_date = fields.Date('Expected Delivery Date')
    card_number = fields.Char('Card Number')
    expiry_date = fields.Date('Expiry Date')

    @api.model
    def _order_fields(self, ui_order):
        res = super(PosOrder, self)._order_fields(ui_order)
        res.exp_delivery_date = ui_order.get('exp_delivery_date')
        res.pos_delivery_type = ui_order.get('pos_delivery_type')
        res.pos_country = int(ui_order.get('pos_country'))

        return res

    @api.model
    def create(self, vals):
        res = super(PosOrder, self).create(vals)
        res['exp_delivery_date'] = PosOrder.exp_delivery_date
        res['pos_delivery_type'] = PosOrder.pos_delivery_type
        res['pos_country'] = PosOrder.pos_country
        return res