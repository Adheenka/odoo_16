# models/waste_equipment.py

from odoo import models, fields

class WasteEquipment(models.Model):
    _name = 'waste.equipment'
    _description = 'Waste Equipment'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
