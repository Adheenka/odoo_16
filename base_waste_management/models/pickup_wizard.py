# wizard/pickup_wizard.py
from odoo import models, fields, api
from odoo.http import request


class PickupWizard(models.TransientModel):
    _name = 'pickup.wizard'
    _description = 'Pick Up Wizard'

    lead_id = fields.Many2one('sale.order', string='Sale Order', required=True)
    pickup_date = fields.Datetime(string='Pick Up Date', required=True)
    pickup_point = fields.Char(string='Pick Up Point', required=True)
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', required=True)
    driver_id = fields.Many2one('res.partner', string='Driver', required=True)
    equipment_id = fields.Many2one('fleet.equipment',  string='Equipment' )
    receiving_id = fields.Many2one('waste.receiving', string='Waste Receiving Facility')



    def default_get(self, fields):
        res = super(PickupWizard, self).default_get(fields)
        lead_id = self.env.context.get('default_lead_id')
        if lead_id:
            res.update({
                'lead_id': lead_id,
            })
        return res

    def action_confirm(self):
        print('hello')
        # Retrieve the lead_id to update the specific sale order
        lead_id = self.lead_id.id
        if lead_id:
            lead = self.env['sale.order'].browse(lead_id)
            lead.write({
                'state': 'pick_up_scheduled',
                'driver_id':self.driver_id,
                'vehicle_id':self.vehicle_id,
                'pickup_point':self.pickup_point,
                'pickup_date': self.pickup_date,
                'equipment_id': self.equipment_id,
                'receiving_id': self.receiving_id,

            })
        return {'type': 'ir.actions.act_window_close'}