# models/crm_lead_extension.py

from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    waste_type = fields.Many2one('product.category', string='Waste Type')
    volume = fields.Char(string='Volume')

    def action_new_quotation(self):
        self.ensure_one()
        action = self.env.ref('sale_crm.sale_action_quotations_new').read()[0]
        action['context'] = {
            # 'default_partner_id': self.partner_id.id,
            # 'default_opportunity_id': self.id,
            'default_waste_type': self.waste_type.id,
            'default_volume': self.volume,
        }
        return action