# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': 'OpenEduCat Notice Board Enterprise',
    'version': '14.0.1.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Notice Board',
    'complexity': "easy",
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_core_enterprise',
        'openeducat_parent_enterprise'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/op_security.xml',
        'data/notice_sequence_number.xml',
        'data/notice_email_template.xml',
        'views/assets.xml',
        'views/op_notice_group_view.xml',
        'views/op_notice_view.xml',
        'views/op_circular_view.xml',
        'views/op_notice_portal.xml',
        'menu/notice_board_menu.xml',
        'menu/portal_menu_data.xml'
    ],
    'demo': [
        'demo/notice_group_demo.xml',
        'demo/circular_demo.xml',
        'demo/notice_demo.xml',
    ],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 50,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'live_test_url': 'https://www.openeducat.org/plans'
}
