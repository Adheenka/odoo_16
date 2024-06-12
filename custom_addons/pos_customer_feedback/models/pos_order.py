
from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    rating = fields.Char(string='Rating', help="Provide your ratings", compute='_compute_rating')
    comment = fields.Text(string='Comments',  readonly=True, help="Provide the feedbacks in comments")
    feedback = fields.Char(string='Feedback', readonly=True,help="Please provide your feedback")
    delivery_country = fields.Many2one('res.country', readonly=True, string='Delivery Country')
    delivery_type = fields.Selection([
        ('domestic', 'Domestic'),
        ('international', 'International'),
    ], readonly=True, string='Delivery Type')
    expected_delivery_date = fields.Date(string='Expected Delivery Date', readonly=True)

    # def _order_fields(self, ui_order):
    #     res = super()._order_fields(ui_order)
    #
    #     # Check if the value is 'Select' and handle accordingly
    #     if ui_order.get('delivery_type') == 'Select':
    #         res['delivery_type'] = False  # Set a default value or skip the assignment
    #     else:
    #         res['delivery_type'] = ui_order.get('delivery_type')
    #
    #     # Assign other fields as needed
    #     res['feedback'] = ui_order.get('customer_feedback')
    #     res['comment'] = ui_order.get('comment_feedback')
    #     res['delivery_country'] = ui_order.get('delivery_country')
    #     res['expected_delivery_date'] = ui_order.get('expected_delivery_date')
    #
    #     return res
    def _order_fields(self, ui_order):
        res = super()._order_fields(ui_order)
        res['feedback'] = ui_order.get('customer_feedback')
        res['comment'] = ui_order.get('comment_feedback')
        res['delivery_country'] = ui_order.get('delivery_country')
        res['delivery_type'] = ui_order.get('delivery_type')
        # res['expected_delivery_date'] = ui_order.get('expected_delivery_date')
        return res

    @api.depends('feedback')
    def _compute_rating(self):
        """To print star in pos order based on the rating value
        choosing from pos session"""
        self.rating = False
        if self.feedback:
            self.rating = '\u2B50' * int(self.feedback)


















# class PosOrder(models.Model):
#     """To add feedback fields and store its value in pos order"""
#     _inherit = "pos.order"
#
#     feedback = fields.Char(string='Feedback', readonly=True,
#                            help="Please provide your feedback")
#     rating = fields.Char(string='Rating', help="Provide your ratings",
#                          compute='_compute_rating')
#     comment = fields.Text(string='Comments',  readonly=True,
#                           help="Provide the feedbacks in comments")
#
#     def _order_fields(self, ui_order):
#         """To get the value of field in pos session to pos order"""
#         res = super()._order_fields(ui_order)
#         res['feedback'] = ui_order.get('customer_feedback')
#         res['comment'] = ui_order.get('comment_feedback')
#         return res
#
    # @api.depends('feedback')
    # def _compute_rating(self):
    #     """To print star in pos order based on the rating value
    #     choosing from pos session"""
    #     self.rating = False
    #     if self.feedback:
    #         self.rating = '\u2B50' * int(self.feedback)
