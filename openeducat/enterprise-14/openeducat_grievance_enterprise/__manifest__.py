# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': "OpenEduCat Grievance Enterprise",
    'version': '14.0.1.0',
    'summary': """
       Manage Grievance""",
    'auther': "OpenEduCat Inc",
    'website': 'http://www.openeducat.org',
    'category': 'Education',
    "sequence": 3,
    'depends': ['base',
                'openeducat_core_enterprise',
                'openeducat_parent_enterprise', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'wizard/wizard_action_taken_view.xml',
        'views/grievance_category_views.xml',
        'views/grievance_views.xml',
        'views/grievance_team_views.xml',
        'views/grievance_template.xml',
        'views/grievance_portal_menu.xml',
        'views/assets.xml',
        'menu/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': '99',
    'currency': 'EUR',
    'license': 'Other proprietary',
    'live_test_url': 'https://www.openeducat.org/plans'
}
