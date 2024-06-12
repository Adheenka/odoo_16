from odoo import fields, models

class resConfigInherit(models.Model):
    _inherit='pos.config'

    location=fields.Many2many('sales.location' ,string="Location")

class resConfigInherit(models.TransientModel):
    _inherit='res.config.settings'

    pos_location=fields.Many2many(related="pos_config_id.location" ,string="POS_Location",readonly=False)

    
