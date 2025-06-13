{
    'name': 'Sendcloud Connector',
    'version': '1.0',
    'summary': 'Integrate Sendcloud API with Odoo',
    'depends': ['base'],
    'data': [
        'views/sendcloud_menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'post_init_hook': None,
    'auto_load': False,
}

