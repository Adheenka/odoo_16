# models/crm_lead.py
from odoo import models, fields, api
from odoo.http import request


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    waste_category_id = fields.Many2one('product.category', string='Waste Category')
    volume = fields.Char(string='Volume')

    def action_sale_quotations_new(self):
        if not self.partner_id:
            action = self.env["ir.actions.actions"]._for_xml_id("sale_crm.crm_quotation_partner_action")
            action['context'] = {
                'default_waste_category_id': self.waste_category_id.id,
                'default_volume': self.volume,
            }
            return action
        else:
            action = self.action_new_quotation()
            if 'context' in action:
                action['context'].update({
                    'default_waste_category_id': self.waste_category_id.id,
                    'default_volume': self.volume,
                })
            else:
                action['context'] = {
                    'default_waste_category_id': self.waste_category_id.id,
                    'default_volume': self.volume,
                }
            return action



class Sale(models.Model):
    _inherit = 'sale.order'

    waste_category_id = fields.Many2one('product.category', string='Waste Category')

    volume = fields.Char(string='Volume')
    state = fields.Selection(selection_add=[
        ('pick_up_scheduled', 'Pick Up Scheduled'),
        ('waste_dumped', 'Waste Dumped')

    ])
    driver_id = fields.Many2one('res.partner', string='Driver', domain="[('is_company', '=', False)]")
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    pickup_point = fields.Char(string='Pickup Point')
    pickup_date = fields.Datetime(string='Pick Up Date')
    equipment_id = fields.Many2one('fleet.equipment', string='Equipment')
    receiving_id = fields.Many2one('waste.receiving', string='Waste Receiving Facility')

    # def action_report_saleorder(self):
    #     return self.env.ref('action_report_saleorder').report_action(self)
    def action_open_pickup_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Pick Up Scheduled',
            'res_model': 'pickup.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_lead_id': self.id,
            }
        }

    def action_waste_dump(self):
        self.state = 'waste_dumped'

        return
