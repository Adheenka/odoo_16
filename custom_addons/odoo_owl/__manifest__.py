# -*- coding: utf-8 -*-
{
    'name': "OWL TRAINING",

    'summary': """Owl training""",

    'description': """
        Owl training
    """,
    'sequence': -1,
    'author': "odoo",
    'website': "www.yourcompany.com",
    'category': 'OWL',
    'version': '0.1',
    'depends': ['base',  'web',],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list_views.xml',

    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'odoo_owl/static/src/components/*/*.js',
             'odoo_owl/static/src/components/*/*.xml',
        ],

    },
    'license': 'LGPL-3',
}
