# -*- coding: utf-8 -*-
import base64
import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class WebsitePhoto(http.Controller):

    @http.route('/upload/photo', type='http', auth="public", methods=['POST'], csrf=False, website=True)
    def upload_photo(self, **kwargs):
        """Controller per ricevere l'immagine, l'order_id e il product_id dal form.
           Salva il record in photo.order e aggiunge il prodotto al carrello."""
        try:
            _logger.info("Chiamata a /upload/photo con kwargs=%s", kwargs)

            order_id = kwargs.get('order_id')
            product_id = kwargs.get('product_id')
            uploaded_file = kwargs.get('image')  # deve combaciare con name="image" nel form

            # Verifica dei parametri
            if not order_id or not product_id or not uploaded_file:
                _logger.warning("Parametri mancanti: order_id=%s, product_id=%s, image=%s",
                                order_id, product_id, uploaded_file)
                return "Parametri mancanti"

            # Conversione in interi
            try:
                order_id = int(order_id)
                product_id = int(product_id)
            except ValueError:
                _logger.warning("order_id o product_id non validi: %s, %s", order_id, product_id)
                return "order_id o product_id non valido"

            # Verifica che l'ordine esista
            order = request.env['sale.order'].sudo().browse(order_id)
            if not order.exists():
                _logger.warning("Ordine %s non trovato", order_id)
                return "Ordine non trovato"

            # Legge il contenuto del file e converte in base64
            file_content = uploaded_file.read()
            image_data = base64.b64encode(file_content)

            # Crea il record su photo.order
            request.env['photo.order'].sudo().create({
                'order_id': order.id,
                'image': image_data
            })
            _logger.info("Immagine salvata correttamente su photo.order per ordine %s", order.id)

            # Aggiunge il prodotto al carrello (stesso effetto di "Add to Cart")
            website_order = request.website.sale_get_order(force_create=True)
            website_order._cart_update(
                product_id=product_id,
                add_qty=1,
            )

            # Reindirizza alla pagina carrello (o dove preferisci)
            return request.redirect('/shop/cart')

        except Exception as e:
            _logger.exception("Errore durante l'upload della foto: %s", e)
            return "Internal Server Error: %s" % str(e)
