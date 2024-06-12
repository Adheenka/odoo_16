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
    'name': "Base Waste Management",
    'version': '16.0.1.0.0',
    'category': 'Industries',
    'summary': """Manage your properties by selling, renting and bidding""",
    'description': """The module makes it simple for you to manage
     your properties""",
    'author': "Abrus Networks",
    'company': 'Abrus Networks',
    'maintainer': 'Abrus Networks',
    'depends': ['crm', 'sale','sale_crm', 'fleet', 'product','purchase','report_xlsx'],
    'data': [
        'views/crm_lead_views.xml',
        'views/pickup_wizard_views.xml',
        'views/fleet_equipment_menu.xml',
        'views/fleet_equipment_views.xml',
        'views/change_crm_menu.xml',
        'views/wizard_sale_order_report_form.xml',
        'report/report_sale_order.xml',
        # 'report/report_base_waste_management.xml',
        'security/ir.model.access.csv',

    ],

    'images': ['static/description/icon.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
