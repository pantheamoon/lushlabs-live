from odoo import fields, models

class ProductTemplate(models.Model):
    """Inherit product template to add stock info"""
    _inherit = 'product.template'

    def _get_combination_info(self, combination=False, product_id=False,
                            add_qty=1, parent_combination=False,
                            only_template=False):
        """Add stock details to product page"""
        combination_info = super()._get_combination_info(
            product_id=product_id,
            combination=combination,
            add_qty=add_qty,
            parent_combination=parent_combination,
            only_template=only_template
        )
        
        product = self.env['product.product'].browse(combination_info['product_id'])
        combination_info['stock'] = product.sudo().qty_available
        return combination_info