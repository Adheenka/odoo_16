from odoo import fields, models



class ConfigLocation(models.Model):
    _name = "sales.location"
    _rec_name = "sales_location"

    sales_location = fields.Char(string="Sales Location")



class LoadDatatoPos(models.Model):
    _inherit = "pos.session"

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result.append("sales.location")
        print(result)
        return result

    def _loader_params_sales_location(self):
        return {
            "search_params": {
                "fields": ["sales_location"],
            }
        }

    def _get_pos_ui_sales_location(self, params):
        return self.env["sales.location"].search_read(**params["search_params"])
