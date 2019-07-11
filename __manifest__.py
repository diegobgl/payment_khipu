# -*- coding: utf-8 -*-

{
    'name': 'Khipu Payment Acquirer',
    'category': 'Accounting',
    'author': 'Daniel Santibáñez Polanco',
    'summary': 'Payment Acquirer: Khipu Implementation',
    'website': 'https://globalresponse.cl',
    'version': "1.0.0",
    'description': """Khipu Payment Acquirer""",
    'depends': ['payment'],
    'external_dependencies': {
            'python':[
                #'khipu',
                'urllib3',
            ],
    },
    'data': [
        'views/khipu.xml',
        'views/payment_acquirer.xml',
        #'views/payment_transaction.xml',
        'data/khipu.xml',
    ],
    'installable': True,
    'application': True,
}
