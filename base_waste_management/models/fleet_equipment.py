from odoo import models, fields


class Equipment(models.Model):
    _name = 'fleet.equipment'
    _description = 'Fleet Equipment'

    equipment_name= fields.Char(string='Name', required=True)

    def name_get(self):
        result=[]
        for rec in self:
            name = rec.equipment_name
            result.append((rec.id,name))
        return result

class Equipment(models.Model):
     _name = 'waste.receiving'
     _description = 'Waste Receiving facility'

     waste_receiving_facility = fields.Char(string='Waste Receiving Facility', required=True)
     # pickup_wizard_ids = fields.One2many('pickup.wizard', 'equipment_id', string='Pickup Wizards')
     def name_get(self):
         result = []
         for rec in self:
             name = rec.waste_receiving_facility
             result.append((rec.id, name))
         return result

