# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
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
{
    'name': "Website Portal",
    'version': '16.0.1.0.0',
    'category': 'Industries',
    'summary': """Manage your properties by selling, renting and bidding""",
    'description': """The module makes it simple for you to manage
     your properties""",
    'author': "Abrus Networks",
    'company': 'Abrus Networks',
    'maintainer': 'Abrus Networks',
    # 'website': 'https://cybrosys.com',
    'depends': ['base','portal','property_management_custom'],
    'data': [
       'views/portal_template.xml',
    ],

    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
