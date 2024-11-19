{
    'name': 'Product Image Uploader',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Widget per caricare immagini personalizzate sui prodotti',
    'author': 'Il Tuo Nome',
    'depends': ['website_sale', 'product'],
    'data': [
        'views/product_template_views.xml',
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'product_image_uploader/static/src/js/product_image_widget.js',
            'product_image_uploader/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}