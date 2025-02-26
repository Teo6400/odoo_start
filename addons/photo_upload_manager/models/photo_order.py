from odoo import models, fields

class PhotoOrder(models.Model):
    _name = 'photo.order'
    _description = 'Ordine Foto'

    name = fields.Char(string="Nome")
    order_id = fields.Many2one('sale.order', string="Ordine di Vendita", required=True, ondelete='cascade')
    image = fields.Binary(string="Immagine", required=True)
    confirmed = fields.Boolean(string="Confermata", default=False)
