{
    'name': 'Custom Jobs',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for custom reports in CarWorkshop',
    'sequence': '201',
    'license': 'AGPL-3',
    'author': 'SB',
    'maintainer': 'SB',
    'website': 'sb.com',
    'depends': ['base','fleet', 'fleet_car_workshop',],
    'demo': [],
    'data': [
        'reports/job_sheet.xml'
    ],
    'images': ['static/description/banner.jpg','static/src/img/header.jpeg','static/src/img/footer.jpeg',],
    'installable': True,
    'application': True,
    'auto_install': False,

}
