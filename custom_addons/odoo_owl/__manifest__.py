# -*- coding: utf-8 -*-
{
    'name': "Tuto OWL",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'sequence': -1,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'OWL',
    'version': '16.0.1.0.1',
    'depends': ['base', 'contacts', 'web', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'odoo_owl/static/src/components/*/*owl_study.js',
            'odoo_owl/static/src/components/*/*.scss',
            'odoo_owl/static/src/components/*/*.xml',
        ],

    },
    'license': 'LGPL-3',
}
