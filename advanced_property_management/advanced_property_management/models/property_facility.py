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


class PropertyFacility(models.Model):
    """A class for the model property facilities to represent
    the related facilities for a property"""
    _name = 'property.facility'
    _description = 'Property Facility'
    _rec_name = 'facility'

    facility = fields.Text(string='Facility', required=True,
                           help='Facilities of the property')