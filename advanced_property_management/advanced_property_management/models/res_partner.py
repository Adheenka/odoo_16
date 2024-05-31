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
from odoo import fields, models


class ResPartner(models.Model):
    """A class that inherits the already existing model res partner"""
    _inherit = 'res.partner'

    blacklisted = fields.Boolean(string='Blacklisted', default=False,
                                 help='Is this contact a blacklisted contact '
                                      'or not')

    def action_add_blacklist(self):
        """Sets the field blacklisted to True"""
        self.blacklisted = True

    def action_remove_blacklist(self):
        """Sets the field blacklisted to False"""
        self.blacklisted = False


# property managemnet custom code
    emirates_id = fields.Char('Tenant’s Emirates ID')
    co_occupants = fields.Integer('Number of Co-Occupants')
    license_no = fields.Integer(string="License No")
    license_auth = fields.Char(string="Licensing Authority")