# -*- coding: utf-8 -*-
{
    'name': 'Conti Reports',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for conti reports in sale order lines',
    'sequence': '201',
    'license': 'AGPL-3',
    'author': 'AB',
    'maintainer': 'AB',
    'website': 'ab.com',
    'depends': ['base', 'fleet', 'fleet_car_workshop', 'account', 'account_accountant'],
    'demo': [],
    'data': [
        'reports/invoice.xml',
        'reports/invoice_sheet.xml',
        'views/inherit_cost_product.xml',
    ],
    'images': ['static/description/banner.jpg','static/src/img/header.jpeg','static/src/img/footer.jpeg','static/src/img/paid.png'],
    'installable': True,
    'application': True,
    'auto_install': False,

}