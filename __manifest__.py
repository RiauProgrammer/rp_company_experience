# -*- coding: utf-8 -*-

{
    'name': 'Company Experience',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'Experience Project',
    'author': 'Muhammad Syarif',
    'email': 'mhdsyarif.ms@gmail.com',
    'website': 'https://www.mhdsyarif.com',
    'license': 'AGPL-3',
    'depends': ['contacts','base','mail'],
    'data': [
        'views/rp_experience.xml',
        'security/rp_experience.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/syarif.png'],
    'installable': True,
    'auto_install': False
}