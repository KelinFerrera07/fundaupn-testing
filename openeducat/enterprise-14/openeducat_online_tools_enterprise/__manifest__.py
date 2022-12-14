
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': 'OpenEduCat Online Tools Base Enterprise',
    'version': '14.0.1.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Base Module for Manage Online Teaching Tools',
    'complexity': "easy",
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'depends': [
        'calendar',
        'openeducat_core_enterprise',
        'openeducat_timetable_enterprise',
    ],
    'data': [
        'views/assets.xml',
        'views/timetable_view.xml',
        'views/calender_event.xml',
        'views/online_meeting_portal_view.xml',
        'views/res_config_setting_view.xml',
        'menu/online_meeting_portal_menu.xml',
    ],
    'images': [
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 50,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'live_test_url': 'https://www.openeducat.org/plans'
}
