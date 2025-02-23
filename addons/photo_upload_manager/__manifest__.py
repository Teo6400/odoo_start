{
    'name': 'Photo Upload Manager',
    'version': '1.0',
    'summary': 'Permette di caricare immagini personalizzate su prodotti',
    'description': 'Un modulo per caricare immagini su ordini e visualizzarle nel backend',
    'category': 'Website',
    'author': 'Tuo Nome',
    'depends': ['website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/photo_order_views.xml',
        'views/website_templates.xml',
    ],
    'installable': True,
    'application': True,
}
