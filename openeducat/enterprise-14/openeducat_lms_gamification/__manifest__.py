
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': 'OpenEduCat LMS Gamification',
    'version': '14.0.1.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'LMS',
    'complexity': "easy",
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'depends': [
        'gamification', 'website_profile',
        'openeducat_lms'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/course_view.xml',
        'views/gamification_badges_view.xml',
        'views/assets.xml',
        'views/web_gamification_view.xml',
        'menus/op_menu.xml',
        'menus/badge_portal_menu.xml'
    ],
    'demo': [
        'demo/challenges_data.xml'
    ],
    'images': [
        'static/description/openeducat_lms_gamification_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 30,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'live_test_url': 'https://www.openeducat.org/plans'
}
