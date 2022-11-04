{
    'name': 'OpenEduCat Online Appointments',
    'version': '14.0.1.0',
    'category': 'Website',
    "sequence": 3,
    'summary': 'Online appointments',
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'depends': ['calendar', 'hr', 'website',
                'openeducat_core_enterprise', 'openeducat_qna_mixin'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/mail_template_data.xml',
        'data/menu.xml',
        'views/calendar_online_appointment_view.xml',
        'views/calendar_view.xml',
        'views/appointment_template.xml',
        'views/assets.xml',

    ],
    'demo': [
        'demo/slot.xml',
        'demo/appointment.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 150,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'live_test_url': 'https://www.openeducat.org/plans'
}
