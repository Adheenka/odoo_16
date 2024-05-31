# -*- coding: utf-8 -*-
#############################################################################
#
#    Abrus Networks Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Abrus Networks(<http://www.abrusnetworks.com>)
#    Author: Abrus Networks(<http://www.abrusnetworks.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class PropertyRental(models.Model):
    """A class for the model property rental to represent
    the rental order of a property"""
    _name = 'property.rental'
    _description = 'Property Rent'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reference', readonly=True,
                       required=True, copy=False, default='New',
                       help='The reference code/sequence of the property '
                            'rental')
    property_id = fields.Many2one(
        'property.property', string='Property',
        required=True,
        help='The property to be rented',
        domain="[('state','=','available'),('sale_rent','=','for_tenancy')]")
    owner_id = fields.Many2one('res.partner', string='Land Lord',
                               store=True,
                               help='The owner / land lord of the property')
    rent_price = fields.Monetary(string='Rent Price',

                                 help='The Rental price per month of the '
                                      'property')
    renter_id = fields.Many2one('res.partner', string='Renter', required=True,
                                help='The customer who is renting the property')
    state = fields.Selection(
        [('draft', 'Draft'), ('in_contract', 'In Contract'),
         ('expired', 'Expired'), ('cancel', 'Cancelled')],
        required=True, default='draft', string='Status', tracking=True,
        help="* The \'Draft\' status is used when the rental is in draft.\n"
             "* The \'In Contract\' status is used when the property is rented "
             "and is in contract\n"
             "* The \'Expired\' status is used when the property rented "
             "contract has expired.\n"
             "* The \'Cancelled\' status is used when the property rental "
             "is cancelled.\n")
    start_date = fields.Date(string='Start Date', required=True,
                             help='The starting date of the rent')
    end_date = fields.Date(string='End Date', required=True,
                           help='The Ending date of the rent')
    invoice_count = fields.Integer(strinf='Invoice Count',
                                   compute='_compute_invoice_count',
                                   help='The Invoices related to this rental')
    rental_bills_ids = fields.One2many('rental.bill', 'rental_id')
    invoice_date = fields.Date(string='Invoice Date',
                               help='The latest Invoiced Date')
    next_invoice = fields.Date(string='Next Invoice',
                               compute='_compute_next_invoice',
                               help='The next invoicing date')
    company_id = fields.Many2one('res.company',
                                 string="Property Management Company",
                                 default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  related='company_id.currency_id')

    @api.model
    def create(self, vals):
        """Setting the sequence when record is created"""
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'property.rent') or 'New'
        res = super(PropertyRental, self).create(vals)
        return res

    def _compute_invoice_count(self):
        """Calculates the Invoice count for the property"""
        self.invoice_count = self.env['account.move'].search_count(
            [('property_rental_id', '=', self.id)])

    def _compute_next_invoice(self):
        """Computes the next_invoice date"""
        if self.invoice_date and fields.Date.today() < self.end_date:
            self.next_invoice = fields.Date.add(self.invoice_date, months=1)
        else:
            self.next_invoice = False

    def action_cancel(self):
        """ Changes the record stage to cancel """
        self.property_id.state = 'available'
        self.state = 'cancel'

    def action_create_contract(self):
        """Creates an invoice for contract. Checks if the customer
        is blacklisted."""
        if self.renter_id.blacklisted:
            raise ValidationError(
                _('The Customer %r is Blacklisted.', self.renter_id.name))
        self.env['account.move'].create({
            'move_type': 'out_invoice',
            'property_rental_id': self.id,
            'invoice_line_ids': [fields.Command.create({
                'name': self.property_id.name,
                'price_unit': self.rent_price,
                'currency_id': self.env.user.company_id.currency_id.id,
            })]
        })
        self.invoice_date = fields.Date.today()
        self.property_id.state = 'rented'
        self.state = 'in_contract'

    def action_view_invoice(self):
        """Views all the related invoice in tree view related to the records"""
        return {
            'name': _('Invoices'),
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'target': 'current',
            'type': 'ir.actions.act_window',
            'domain': [('property_rental_id', '=', self.id),
                       ('move_type', '=', 'out_invoice')]
        }

    @api.model
    def action_check_rental(self):
        """Scheduled action to create the next invoice for rent
        else set it as expired."""
        records = self.env['property.rental'].search(
            [('state', '=', 'in_contract')])
        for rec in records:
            if not rec.next_invoice:
                rec.state = 'expired'
            if fields.Date.today() == rec.next_invoice:
                self.env['account.move'].create({
                    'move_type': 'out_invoice',
                    'property_rental_id': rec.id,
                    'invoice_line_ids': [fields.Command.create({
                        'name': rec.property_id.name,
                        'price_unit': rec.rent_price,
                        'currency_id': rec.env.user.company_id.currency_id.id,
                    })]
                })
                rec.invoice_date = fields.Date.today()

# advance property custom code

    company_id = fields.Many2one(
        "res.company",
        string="Property Management Company",
        default=lambda self: self.env.company,
    )
    terms_conditions_ids = fields.One2many('property.terms', 'prop_rental', string='Terms and Conditions')

    @api.model
    def default_get(self, fields):
        defaults = super(PropertyRental, self).default_get(fields)

        terms = self.env['property.terms'].search([])
        term_ids = [(4, term.id) for term in terms]

        defaults['terms_conditions_ids'] = term_ids

        return defaults

    company_currency = fields.Many2one("res.currency", string='Currency', compute="_compute_company_currency",
                                       compute_sudo=True)

    apartment_id = fields.Many2one('property.apartment', string="Apartment",
                                   domain="[('state','=','available'),('property_id','=',property_id)]")
    rent_price = fields.Monetary(string='Annual Price',
                                 store=True, compute="get_rent_price",
                                 help='The Rental price per month of the '
                                      'property', currency_field='company_currency', )

    owner_id = fields.Many2one('property.owner', string='Owner/Lessor', store=True,
                               compute='_compute_owner_id',
                               help='The owner / land lord of the property', domain="_get_owner_domain")

    note = fields.Html(
        string="Terms and conditions",

        readonly=False)
    renter_id = fields.Many2one('res.partner', string='Tenant', required=True,
                                help='The customer who is renting the property')

    related_booking_id = fields.Many2one("apartment.booking", string="Booking ID")

    invoice_policy = fields.Selection(
        [
            ("monthly", "Monthly"),
            ("quarterly", "Quarterly"),

        ],
        string="Invoice Policy",

    )
    number_payment = fields.Integer(string="Number of Payment")
    comment = fields.Text('Comments')
    start_date = fields.Date(string='Contract Period', required=True,
                             help='The starting date of the rent')
    end_date = fields.Date(string='To', required=True,
                           help='The Ending date of the rent')
    contract_value = fields.Monetary(string="Contract Value", currency_field='company_currency',
                                     compute="get_rent_price")
    security_amount = fields.Monetary(string='Security Deposit Amount', currency_field='company_currency')
    unit_num = fields.Integer(string="Unit Number")
    rental_payment = fields.Selection([('received', ' Received'),
                                       ('not_received', 'Not received'),
                                       ], string="Rental Payment")
    security_payment = fields.Selection([('received', ' Received'),
                                         ('not_received', 'Not received'),
                                         ], string="Security Deposit ")
    addc = fields.Selection([('yes', ' Yes'),
                             ('no', 'No'),
                             ], string="ADDC Connected ")
    tawtheeq = fields.Selection([('yes', ' Yes'),
                                 ('no', 'No'),
                                 ], string="Tawtheeq Issued ")
    move_inspection = fields.Selection([('scheduled', 'Scheduled'),
                                        ('not_scheduled', 'Not-Scheduled'),
                                        ], string="Pre-Move-in Inspection")
    move_date = fields.Date(string="Move In Date")
    parking_slot = fields.Integer(string="No. of Car Parking Slots")
    car_brand = fields.Char(string="Brand / Make")
    car_number = fields.Char(string="Car Plate No.")
    model = fields.Char(string="Model")
    car_color = fields.Char(string="Car Color")
    contract_id = fields.Many2one('property.rental', string="contract Id")
    created_permit = fields.Boolean(string="permit created", default=False)

    payment_type = fields.Selection(
        [
            ("bank", "Bank"),
            ("cash", "Cash"),

        ],
        string="Mode of Payment",

    )
    show_ap = fields.Boolean(strng="show", compute="get_rental_apart")
    access_count = fields.Integer(compute='_compute_access_count')
    parking_allocation_count = fields.Integer(compute='_compute_parking_count')

    def _compute_access_count(self):
        for rec in self:
            rec.access_count = self.env['access.card.key.receipt'].search_count([('contract_id', '=', rec.id)])

    def _compute_parking_count(self):
        for rec in self:
            rec.parking_allocation_count = self.env['parking.allocation'].search_count([('contract_id', '=', rec.id)])

    def action_get_access_key(self):
        print("oooo")
        context = {
            'default_tenant_name': self.renter_id.id,
            'default_property_name_id': self.property_id.id,
            'default_building_name_id': self.apartment_id.id,
            'default_contract_id': self.id,

        }
        return {
            "name": "Access Cards/Key Receipt",
            "view_mode": "tree,form",
            "res_model": "access.card.key.receipt",
            "type": "ir.actions.act_window",
            "domain": [("contract_id", "=", self.id)],
            'context': context,
        }

    @api.depends('show_ap', 'property_id', 'apartment_id')
    def _compute_owner_id(self):
        for record in self:
            if record.show_ap:
                record.owner_id = record.apartment_id.owner_id.id
            else:
                record.owner_id = record.property_id.landlord_id.id

    @api.onchange('property_id')
    def get_rental_apart(self):
        show_ap = False
        for rec in self:
            if rec.property_id:
                if rec.property_id.property_category == "apartment":
                    show_ap = True
            rec.show_ap = show_ap

    @api.depends('apartment_id', 'property_id')
    def get_rent_price(self):
        for rec in self:
            if rec.property_id.property_category == "villa":
                rec.rent_price = rec.property_id.rent_month
                # rec.owner_id = rec.property_id.landlord_id.id
            else:
                if rec.property_id.property_category == "apartment":
                    rec.rent_price = rec.apartment_id.rent_month
                    # rec.owner_id = rec.apartment_id.owner_id.id
            rec.contract_value = rec.rent_price

    @api.depends('company_id')
    def _compute_company_currency(self):
        for lead in self:
            if not lead.company_id:
                lead.company_currency = self.env.company.currency_id
            else:
                lead.company_currency = lead.company_id.currency_id
                print('jgfhghfjh')

    # @api.onchange('property_id','apartment_id')
    # def change_property_type(self):
    #     if self.apartment_id:
    #         if self.apartment_id.rent_month:
    #             self.rent_price =  self.apartment_id.rent_month
    #             self.contract_value = self.apartment_id.rent_month
    #         if self.apartment_id.owner_id:
    #             self.owner_id = self.apartment_id.owner_id
    #     else:
    #         if self.property_id.rent_month:
    #             self.rent_price =  self.property_id.rent_month
    #             self.contract_value = self.property_id.rent_month
    #         if self.property_id.landlord_id:
    #             self.owner_id = self.property_id.landlord_id

    # rent_price = fields.Monetary(string='Annual Rent',
    #                              related='property_id.rent_month',
    #                              help='The Rental price per month of the '
    #                                   'property')

    # def action_create_contract(self):
    #     """Creates an invoice for contract. Checks if the customer
    #     is blacklisted."""
    #     if self.renter_id.blacklisted:
    #         raise ValidationError(
    #             _('The Customer %r is Blacklisted.', self.renter_id.name))
    #     self.env['account.move'].create({
    #         'move_type': 'out_invoice',
    #         'property_rental_id': self.id,
    #         'partner_id': self.renter_id.id,
    #         'invoice_line_ids': [fields.Command.create({
    #             'name': self.property_id.name,
    #             'price_unit': self.rent_price,
    #             'currency_id': self.env.user.company_id.currency_id.id,
    #         })]
    #     })
    #     self.invoice_date = fields.Date.today()
    #     self.apartment_id.state = 'rented'
    #     self.state = 'in_contract'
    from datetime import datetime, timedelta

    from datetime import datetime, timedelta
    # property webpage inherit  url mateet backend

    def action_create_contract(self):
        """Creates invoices based on the specified number of payments."""
        if self.renter_id.blacklisted:
            raise ValidationError(_('The Customer %r is Blacklisted.', self.renter_id.name))

        start_date = self.start_date
        end_date = self.end_date

        num_payments = self.number_payment
        if num_payments <= 0:
            raise ValidationError(_('Number of payments should be greater than zero.'))

        payment_interval = (end_date - start_date) / num_payments

        for i in range(num_payments):
            payment_start_date = start_date + (payment_interval * i)
            payment_end_date = min(payment_start_date + payment_interval - timedelta(days=1), end_date)

            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'property_rental_id': self.id,
                'partner_id': self.renter_id.id,
                'invoice_line_ids': [fields.Command.create({
                    'name': self.property_id.name,
                    'price_unit': self.rent_price / num_payments,
                    'currency_id': self.env.user.company_id.currency_id.id,
                })],
                'invoice_date': payment_start_date,
                'invoice_date_due': payment_end_date,
                'invoice_origin': 'Contract Invoice',
            })
            invoice.action_post()

        self.related_booking_id.state = 'booked'
        if self.property_id.property_category == "villa":
            self.property_id.state = 'rented'
        elif self.property_id.property_category == "apartment":
            self.apartment_id.state = 'rented'
        self.state = 'in_contract'

    def action_cancel(self):
        """ Changes the record stage to cancel """
        if self.property_id.property_category == "villa":
            self.property_id.state = 'available'
        elif self.property_id.property_category == "apartment":
            self.apartment_id.state = 'available'
        self.state = 'cancel'

    # def action_view_pdc(self):
    #     renter = self.renter_id
    #     return {
    #         "name": "PDC",
    #         "view_mode": "form,tree",
    #         "res_model": "pdc.wizard",
    #         "type": "ir.actions.act_window",
    #         "context": {
    #             'default_partner_id': renter.id}
    #
    #     }

    def action_view_journal(self):
        default_journal = self.env['account.journal'].search([('id', '=', 3), ('type', '=', 'general')], limit=1)
        print(default_journal, 'pppp')
        default_journal_id = default_journal.id if default_journal else False

        return {
            "name": "Journal",
            "view_mode": "form,tree",
            "res_model": "account.move",
            "type": "ir.actions.act_window",
            "context": {
                'default_move_type': 'entry',
                'search_default_posted': 1,
                'view_no_maturity': True,
                'default_journal_id': default_journal_id,
            }
        }

    def action_view_parking_allocation(self):
        property = self.property_id
        apartment = self.apartment_id
        return {
            "name": "Parking Allocation",
            "view_mode": "tree,form",
            "res_model": "parking.allocation",
            "type": "ir.actions.act_window",
            "domain": [("contract_id", "=", self.id)],
            "context": {
                'default_property_name': property.id,
                'default_apartment_name': apartment.id,
                'default_contract_id': self.id}

        }

    def print_move_permit(self):
        action = {
            'name': _('Move Permit'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'permit.wizard',
            'target': 'new',
            'context': {'default_contract_id': self.id,
                        'default_tenent_name': self.renter_id.id},
        }
        return action

    def print_move_permit_report(self):
        return self.env.ref('advanced_property_management.action_report_move_permit').report_action(self, data={})

    def print_rental_contract(self):
        if self.property_id.emirate_state == 'dubai':
            return self.env.ref('advanced_property_management.report_contract_rental').report_action(self, data={})
        elif self.property_id.emirate_state == 'abu_dhabi':
            return self.env.ref('advanced_property_management.report_contract_rental_second').report_action(self, data={})


class InvoiceRental(models.Model):
    """A class for the model property rental to represent
    the rental order of a property"""
    _inherit = 'account.move'

    property_id = fields.Many2one('property.property' ,string="Property")
    apartment_id = fields.Many2one('property.apartment', string="Apartment")