from odoo import models

class QtySession(models.Model):
    _inherit='pos.session'

    def _loader_params_product_product(self):
        res = super()._loader_params_product_product()
        res.get('search_params').get('fields').append('qty_available')
        print(res,"=========================")
        return res