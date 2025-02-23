from odoo import models, fields

class PhotoOrder(models.Model):
    _name = 'photo.order'
    _description = 'Ordine Foto'

    # Campo "name" opzionale, utile se vuoi dare un nome al record
    name = fields.Char(string="Nome")

    order_id = fields.Many2one('sale.order', string="Ordine di Vendita", required=True, ondelete='cascade')
    image = fields.Binary(string="Immagine", required=True)
