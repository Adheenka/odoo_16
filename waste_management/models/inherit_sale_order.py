# models/sale_order_extension.py

from odoo import models, fields
from odoo.odoo.exceptions import UserError


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
            },
            'name': 'Pickup Scheduled',
        }

    def action_waste_dumped(self):
        self.ensure_one()
        self.write({'state': 'waste_dumped'})

    # def _prepare_invoice(self):
    #     invoice_vals = super(SaleOrder, self)._prepare_invoice()
    #     # Add custom fields to the invoice if needed
    #     return invoice_vals
    #
    # def action_invoice_create(self):
    #     # Custom logic to handle custom states
    #     if self.state not in ['pickup_scheduled', 'waste_dumped']:
    #         raise UserError("You cannot create an invoice in the current state.")
    #     return super(SaleOrder, self).action_invoice_create()