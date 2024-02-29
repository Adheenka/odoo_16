# -*- coding: utf-8 -*-

{
    'name': 'pos_inheritence',
    'version': '1.0.0',
    'category': 'Sales/Sales',
    'author': 'adheen',
    'sequence': -90,
    'summary': 'pos_inheritence',
    'description': """ pos management system
""",
    'depends': ['point_of_sale'],
    'data': [

        'views/res_partner_view.xml',
        'views/pos_bank_details.xml',



    ],
    'assets': {
        'point_of_sale.assets': [
           "pos_inheritence/static/src/js/DeliveryDetailsButton.js",
           "pos_inheritence/static/src/xml/DeliveryDetailsButton.xml",
           "pos_inheritence/static/src/js/DeliveryDetailsPopup.js",
           "pos_inheritence/static/src/xml/DeliveryDetailsPopup.xml",
           "pos_inheritence/static/src/js//payment_inherit.js",

        ],
    },

    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',


}

