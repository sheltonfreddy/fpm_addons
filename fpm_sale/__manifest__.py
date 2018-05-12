# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'FPM Sales Reports',
    'version': '1.0',
    'category': 'Sales',
    'sequence': 15,
    'summary': 'FPM Sales Reports',
    'depends': ['sale'],
    'data': [
        'report/sale_report_templates.xml',
        'report/sale_report.xml',
    ],
    'installable': True,
    'auto_install': False
}
