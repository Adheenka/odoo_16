from odoo import fields, models, api, exceptions

class PosCustomData(models.Model):
    _inherit = 'res.partner'

    mobile_no = fields.Char("Phone Number")

    @api.constrains('mobile_no')
    def _check_unique_mobile(self):
        for order in self:
            if order.mobile_no:
                duplicate_orders = self.search([
                    ('mobile_no', '=', order.mobile_no),
                    ('id', '!=', order.id),
                ])
                if duplicate_orders:
                    raise exceptions.ValidationError("Mobile number must be unique per customer.")
                
class PosCustomSession(models.Model):
    _inherit='pos.session'

    def _loader_params_res_partner(self):
        res = super()._loader_params_res_partner()
        res.get('search_params').get('fields').append('mobile_no')
        return res
 

    