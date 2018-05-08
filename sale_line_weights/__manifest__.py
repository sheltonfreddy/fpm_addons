# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sales Line Weights',
    'version': '1.0',
    'category': 'Sales',
    'sequence': 15,
    'summary': 'Sales Line Weight',
    'depends': ['sale'],
    'data': [
        'views/sale_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
