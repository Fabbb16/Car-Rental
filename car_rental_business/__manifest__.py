# -*- coding: utf-8 -*-
{
    'name': "shitesi",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'installable': True,
    'application': True,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/gift_views.xml',
        'views/order_views.xml',
        'views/review_views.xml',
        'views/1_templates.xml',
        'views/2_templates.xml',
        'views/3_templates.xml',
        'views/4_templates.xml',
        'views/5_templates.xml'
    ]
}

