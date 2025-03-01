{
    'name': 'Photo Upload Manager',
    'version': '1.0',
    'summary': 'Gestione upload immagini su prodotti con conferma automatica',
    'description': """
        Modulo per caricare immagini personalizzate sugli ordini
        e gestire la conferma automatica delle immagini.
    """,
    'category': 'Website',
    'author': 'Tuo Nome',
    'depends': [
        'sale',
        'sale_management',
        'website_sale',
        
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/photo_order_views.xml',
        'views/website_templates.xml',
        'data/automated_action.xml',
    ],
    'installable': True,
    'application': True,
}
