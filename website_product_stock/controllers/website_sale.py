from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSale(WebsiteSale):
    """to pass stock details to shop page"""

    @http.route()
    def shop(self, **post):
        """To include stock values during rendering of the shop page."""
        result = super().shop(**post)
        products = result.qcontext.get('products', [])
        result.qcontext['stocks'] = {
            product: self.get_stock_info(product) 
            for product in products
        }
        return result

    def get_stock_info(self, product):
        """function to get stock details"""
        if product.type == 'service':
            return 'N/A'
        combination_info = product._get_combination_info()
        return combination_info.get('stock', 0)