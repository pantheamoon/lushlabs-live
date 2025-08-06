# -*- coding: utf-8 -*-

{
    'name': "Show Stock on Website ",
    'version': '18.0.1.0.1',
    'category': 'Website',
    'summary': 'Allows users to see stock details of products from the website',
    'description': """Helps to display the stock details of each product on 
     the website. It includes options to show product stock information 
     conditionally based on predefined location types and stock types.""",
    'author': 'Epicore Systems',
    'company': 'Epicore Systems',
    'maintainer': 'Epicore Ssystems',
    'website': "https://www.epicoresys.com",
    'depends': ['base', 'website', 'website_sale_stock'],
    'data': [
        'views/product_stock_information_snippet.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
