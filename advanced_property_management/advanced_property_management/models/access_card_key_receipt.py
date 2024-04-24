from odoo import api, fields, models, _

class AccessCardKey(models.Model):

    _name = "access.card.key.receipt"
    _rec_data = 'name'

    tenant_name = fields.Many2one('res.partner','Tenant Name')
    contract_id = fields.Many2one('property.rental',string='Rental Contract',domain="[('state', '=','in_contract' )]")
    name = fields.Char(
        string="Reference",
        readonly=True,
        copy=False,
        default=lambda self: _("New"),

    )
    mobile_number = fields.Char('Mobile Number')
    phone_number = fields.Char('Phone Number')
    property_name_id = fields.Many2one('property.property',string='Property Name')
    building_name_id = fields.Many2one('property.apartment',string='Apartment Name',
                                       domain="[('property_id', '=',property_name_id )]"
    )
    unit_description = fields.Char('Unit Description')
    building_number = fields.Char('Apartment Number')
    unit_no = fields.Char('Unit Number')
    key_received = fields.One2many('key.received.line','key_id',string="Key Received")
    access_card = fields.One2many('access.card.line','access_id',string="Access Card")
    additional_card_req = fields.One2many('additional.card.line','card_id',string="Additional Card Requested")
    other_information = fields.One2many('other.info.line','info_id',string="Other Information")

    @api.model
    def create(self, vals):
        """Generating sequence number at the time of creation of record"""
        if vals.get("name", "New") == "New":
            vals["name"] = (
                    self.env["ir.sequence"].next_by_code("access.card.key.receipt") or "New"
            )
        res = super(AccessCardKey, self).create(vals)
        return res

    def button_access_key(self):
        return self.env.ref('property_management_custom.report_access_card_key').report_action(self, data={})


class KeyReceived(models.Model):

    _name = "key.received.line"

    key_id = fields.Many2one('access.card.key.receipt')
    key_name = fields.Char('Key')
    key_type = fields.Char('Type')

class AccessCard(models.Model):

    _name = "access.card.line"

    access_id = fields.Many2one('access.card.key.receipt')
    card_name = fields.Char('Card')
    serial_no = fields.Char('Serial Number')

class AdditionalCardRequested(models.Model):

    _name = "additional.card.line"

    card_id = fields.Many2one('access.card.key.receipt')
    card_name = fields.Char('Card')
    serial_no = fields.Char('Serial Number')

class Otherinformation(models.Model):

    _name = "other.info.line"

    info_id = fields.Many2one('access.card.key.receipt')
    card_holder_name = fields.Char('Card Holder Name')
    mobile_no = fields.Char('Mobile Number')


