# models/waste_equipment.py

from odoo import models, fields

class WasteEquipment(models.Model):
    _name = 'waste.equipment'
    _description = 'Waste Equipment'

    equipment_name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    def name_get(self):
        result = []
        for rec in self:
            name = rec.equipment_name
            result.append((rec.id, name))
        return result