# -*- coding: utf-8 -*-
{
    'name': "Provider Withdrawal",

    'summary': """
        Create report by provider
        """,

    'description': """
        Create a module that return a list of product belongings to a selected provider.
        Return the status of each product in the point of sale and the sales total amount.
    """,

    'author': "Florian",
    'website': "https://odoo.fp-ws.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'purchase'],
    "application": True,
    "auto_install": False,
    "installable": True,
    'license': 'AGPL-3',
    "images": ['static/description/icon.png'],
    # always loaded
    'data': [
        'report/withdrawal_report_template.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}