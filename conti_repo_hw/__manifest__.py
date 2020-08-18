# -*- coding: utf-8 -*-
{
    'name': 'Conti home world Reports',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for conti reports home world in sale order lines',
    'sequence': '202',
    'license': 'AGPL-3',
    'author': 'AB',
    'maintainer': 'AB',
    'website': 'ab.com',
    'depends': ['base', 'fleet', 'fleet_car_workshop', 'account', 'account_accountant','customize_invoice', 'stock','conti_repo'],
    'demo': [],
    'data': [
        'views/views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}