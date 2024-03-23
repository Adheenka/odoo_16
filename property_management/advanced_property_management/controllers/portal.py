from operator import itemgetter

from odoo import _, http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.osv.expression import AND, OR
from odoo.tools import groupby as groupbyelem

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

from odoo.addons.portal.controllers import portal

class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):

        values = super()._prepare_home_portal_values(counters)
        if "booking_count" in counters:
            helpdesk_model = request.env["apartment.booking"]
            booking_count = (
                        helpdesk_model.search_count([])
                    )
            values["booking_count"] = booking_count
        return values

    # def _prepare_home_portal_values(self, counters):
    #     values = super()._prepare_home_portal_values(counters)
    #     if 'pre_booking_count' in counters:
    #         apartment_booking_model = http.request.env['apartment.booking']
    #         pre_booking_count = (
    #             apartment_booking_model.search_count([])
    #             if apartment_booking_model.check_access_rights("read", raise_exception=False)
    #             else 0
    #         )
    #         values['pre_booking_count'] = pre_booking_count
    #     return values

# class RentalRequests(CustomerPortal):
#     def _prepare_home_portal_values(self, counters):
#         values = super()._prepare_home_portal_values(counters)
#         if "request_count" in counters:
#             helpdesk_model = request.env["apartment.booking"]
#             request_count = (
#                 helpdesk_model.search_count([])
#             )
#             values["request_count"] = request_count
#         return values
#
#
class Requests(http.Controller):
    @http.route('/my/request', auth='public', website=True)
    def rental_requests(self, ):
        print("waiting requests")
        return request.render("advanced_property_management.portal_my_rental")
        """ Shows each corresponding properties view in property_view_item """








































    # def _prepare_home_portal_values(self, counters):
    #     values = super()._prepare_home_portal_values(counters)
    #     if 'booking_count' in counters:
    #         current_user = request.env['res.users'].sudo().browse(
    #             request.env.uid)
    #         booking_model = request.env["apartment.booking"]
    #
    #         booking_count = request.env['apartment.booking'].search_count(
    #             [('partner_id', '=', current_user.partner_id.id)])
    #         values['booking_count'] = booking_count
    #     return values
