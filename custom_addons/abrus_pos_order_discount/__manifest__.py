# -*- coding: utf-8 -*-
{
    'name': "Order Discount",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','sale','point_of_sale','pos_disable_payments'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos_order_view.xml',
        'views/hr_view.xml',
        # 'views/assets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'abrus_pos_order_discount/static/src/js/product_screen.js',
            'abrus_pos_order_discount/static/src/js/discountpopup.js',
            'abrus_pos_order_discount/static/src/js/pos_model.js',
            'abrus_pos_order_discount/static/src/xml/popup.xml',
        ],
    },

}
