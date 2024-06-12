from odoo import fields, http
from odoo.http import request

from odoo.addons.portal.controllers.portal import CustomerPortal


class RentalRequests(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if "request_count" in counters:
            helpdesk_model = request.env["apartment.booking"]
            request_count = (
                helpdesk_model.search_count([])
            )
            values["request_count"] = request_count
        return values




class Requests(http.Controller):
    @http.route('/my/rental', auth='public', website=True)
    def rental_requests(self, ):
        rental_model = request.env["apartment.booking"]
        rentals = rental_model.search([])
        return request.render("website_portal.portal_my_rental_tree", {'rental': rentals})

    # @http.route('/my/rental/form/<int:rental_id>', auth='public', website=True)
    # def rental_form(self, rental_id):
    #     rental_model = http.request.env["apartment.booking"]
    #     rental = rental_model.sudo().browse(rental_id)
    #     return http.request.render("website_portal.portal_my_rental_form_view", {'rental': rental})

    @http.route(['/my/rentals/<model("apartment.booking"):rental_id>'], auth="user", type='http', website=True)
    def rentalFormView(self, rental_id, **kw):
        # Prepare the values to be passed to the template
        vals = {"rental": rental_id, 'page_name': 'rental_form_view'}

        # Render the template with the prepared values
        return http.request.render("website_portal.portal_my_rental_form_view", vals)

# class Requests(http.Controller):
#     @http.route('/my/request', auth='public', website=True)
#     def rental_requests(self, ):
#         print("waiting requests")
#         return request.render("website_portal.portal_my_rental")
#         """ Shows each corresponding properties view in property_view_item """
