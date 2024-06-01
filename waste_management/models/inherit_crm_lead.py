# models/crm_lead_extension.py

from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    waste_type = fields.Many2one('product.category', string='Waste Type')
    volume = fields.Char(string='Volume')
