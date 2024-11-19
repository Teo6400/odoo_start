from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    allow_image_upload = fields.Boolean(
        string='Permetti caricamento immagine',
        default=False
    )
