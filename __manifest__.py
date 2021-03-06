# -*- coding: utf-8 -*-
{
    'name': "gimnasio",

    'summary': """
        Gestión de Gimnasio""",

    'description': """
        Gestión de Gimnasio: Vistas, restricciones, etc
    """,

    'author': "Iván Rodríguez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gimnasio',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/clase_view.xml',
        'views/usuario_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    
    # OJO! Esta línea NO VIENE en el __manifest__ original de Odoo
    'application': True,
    
}