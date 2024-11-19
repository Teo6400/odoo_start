from odoo import http
from odoo.http import request

class ProductImageUploader(http.Controller):

    @http.route('/upload_image', type='http', auth='public', methods=['POST'], csrf=False)
    def upload_image(self, **kwargs):
        file = kwargs.get('custom_image')
        if file:
            # Salva il file in un allegato o elaboralo
            attachment = request.env['ir.attachment'].create({
                'name': file.filename,
                'datas': file.read().encode('base64'),
                'res_model': 'product.template',
                'res_id': int(kwargs.get('product_id')),
            })
            return http.Response("Successo", status=200)
        return http.Response("Errore", status=400)
