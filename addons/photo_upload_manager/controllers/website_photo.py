import base64
import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class WebsitePhoto(http.Controller):

    @http.route('/upload/photo', type='http', auth="public", methods=['POST'], csrf=False)
    def upload_photo(self, **kwargs):
        """Controller per ricevere l'immagine e l'order_id dal form e salvare il record in photo.order."""
        try:
            _logger.info("Chiamata a /upload/photo con kwargs=%s", kwargs)

            order_id = kwargs.get('order_id')
            uploaded_file = kwargs.get('image')  # deve combaciare con name="image" nel form

            # Se mancano parametri, esci
            if not order_id or not uploaded_file:
                _logger.warning("Parametri mancanti: order_id=%s, image=%s", order_id, uploaded_file)
                return "Parametri mancanti"

            # Converto order_id in intero
            try:
                order_id = int(order_id)
            except ValueError:
                _logger.warning("order_id non valido: %s", order_id)
                return "order_id non valido"

            # Controllo che l'ordine esista
            order = request.env['sale.order'].sudo().browse(order_id)
            if not order.exists():
                _logger.warning("Ordine %s non trovato", order_id)
                return "Ordine non trovato"

            # Leggo il contenuto del file e lo converto in base64
            file_content = uploaded_file.read()
            image_data = base64.b64encode(file_content)

            # Creo il record su photo.order
            request.env['photo.order'].sudo().create({
                'order_id': order.id,
                'image': image_data
            })

            _logger.info("Immagine salvata correttamente su photo.order per ordine %s", order.id)
            return http.redirect_with_hash('/shop/cart')

        except Exception as e:
            _logger.exception("Errore durante l'upload della foto: %s", e)
            return "Internal Server Error: %s" % str(e)
