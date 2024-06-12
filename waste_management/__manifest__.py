# -*- coding: utf-8 -*-
{
    'name': "waste_management",

    'summary': 'Module for managing waste resources and disposal',

    'description': """
        A module to handle various aspects of waste management including resource tracking,
        collection, and reporting.
    """,
    'author': "Abrus digital",
    'website': "https://www.yourcompany.com",
    'sequence': -100,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'sale_crm', 'purchase', 'crm', 'sale', 'product', 'fleet','website'],
    'images': ['static/description/icon.png'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_crm_lead_form.xml',
        'views/inherit_sale_order_views.xml',
        'views/waste_equipment_view.xml',
        'views/waste_receving_view.xml',
        'views/crm_menu_view.xml',
        'views/sale_report_wizard.xml',
        'wizard/pickup_schedule_wizard_view.xml',


    ],


    'installable': True,
    'application': True,
}
