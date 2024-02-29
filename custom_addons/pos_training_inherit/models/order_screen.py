from odoo import models, fields, api


class InheritOrderScreeen(models.Model):
    _inherit = ["pos.order"]

    details = fields.Char("Type of Business")
    orderline_location = fields.Many2one("sales.location", readonly=True)

    @api.model
    def _order_fields(self, ui_order):
        _older_fields = super(InheritOrderScreeen, self)._order_fields(ui_order)
        _older_fields.update(
            {
                "details": ui_order.get("details"),
                "orderline_location": ui_order.get("s_loc").get("id"),
            }
        )
        return _older_fields
