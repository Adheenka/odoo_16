# models/sale_order_extension.py

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    waste_type = fields.Many2one('product.category', string='Waste Type')
    volume = fields.Char(string='Volume')
    state = fields.Selection(selection_add=[
        ('pickup_scheduled', 'Pickup Scheduled'),
        ('waste_dumped', 'Waste Dumped')
    ])
    driver_id = fields.Many2one('res.partner', string='Driver')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    def action_pickup_scheduled(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'pickup.schedule.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
                'default_waste_type': self.waste_type.id,
                'default_volume': self.volume,
            }
        }

    def action_waste_dumped(self):
        self.ensure_one()
        self.write({'state': 'waste_dumped'})