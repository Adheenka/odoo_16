from odoo import api, fields, models, _


class AProperty_Owner(models.Model):
    _name = "property.owner"
    _description = "Owner/Lessor"
    _rec_name = "owners_name"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    owners_name = fields.Char(string="Owner's Name")
    lessor_name = fields.Char(string="Lessor’s Name")
    emirates_id = fields.Char('Lessor’s Emirates ID')
    lessor_type = fields.Selection(string='Lessor Type',
                                   selection=[('person', 'Individual'), ('company', 'Company')], default="person")
    license_no = fields.Integer(string="License No")
    license_auth = fields.Char(string="Licensing Authority")
    lessor_email = fields.Char(string="Email")
    lessor_phone = fields.Char(string="Phone")
    active = fields.Boolean(default=True)
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    country_code = fields.Char(related='country_id.code', string="Country Code")


class Parking_allocation(models.Model):
    _name = "parking.allocation"
    _description = "Owner/Lessor"
    _rec_name = "property_name"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    property_name = fields.Many2one("property.property", string="Property Name")
    apartment_name = fields.Many2one("property.apartment", string="Apartment Name")
    building_name = fields.Char(string="Building Name")
    unit_description = fields.Char('Unit Description')
    building_num = fields.Char(string='Building Number ',
                                   )
    unit_num = fields.Integer(string="Unit No. ")
    car_space_num = fields.Char(string="Car Space (s) No. ")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("allocate", "Allocated"),

        ],
        required=True,
        string="Status",
        default="draft",

    )
    company_id = fields.Many2one(
        "res.company",
        string="Property Management Company",
        default=lambda self: self.env.company,
    )
    contract_id = fields.Many2one("property.rental", string="Contract Name",domain="[('state', '=','in_contract' )]")

    def action_allocate_space(self):
        """Set the state to available"""
        self.state = "allocate"

    def print_parking_allocation(self):
        return self.env.ref('advanced_property_management.report_parking_allocation').report_action(self, data={})