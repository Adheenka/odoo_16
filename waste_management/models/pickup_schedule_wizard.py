# models/pickup_schedule_wizard.py

from odoo import models, fields, api

class PickupScheduleWizard(models.TransientModel):
    _name = 'pickup.schedule.wizard'
    _description = 'Pickup Schedule Wizard'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order', required=True)
    pickup_date = fields.Datetime(string='Pickup Date', required=True)
    pickup_point = fields.Char(string='Pickup Point', required=True)
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', required=True)
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    driver_id = fields.Many2one('res.partner', string='Driver', compute='_compute_driver_id', store=True)
    equipment_ids = fields.Many2many('waste.equipment', string='Equipments')

    @api.depends('vehicle_id')
    def _compute_driver_id(self):
        for record in self:
            if record.vehicle_id:
                record.driver_id = record.vehicle_id.driver_id
            else:
                record.driver_id = False

    def action_confirm(self):
        sale_order = self.sale_order_id
        sale_order.write({
            'state': 'pickup_scheduled',
            # Optionally, store other wizard fields in sale order or perform other actions
        })
