
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': 'OpenEduCat Achievement Enterprise',
    'version': '14.0.1.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Achievement',
    'complexity': "easy",
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_core_enterprise',
        'openeducat_student_progress_enterprise',
    ],
    'data': [
        'security/op_security.xml',
        'security/ir.model.access.csv',
        'wizards/progression_achievement_wizard_view.xml',
        'views/achievement_view.xml',
        'views/achievement_type_view.xml',
        'views/student_view.xml',
        'views/openeducat_achievement_portal.xml',
        'views/openeducat_progression_achievement.xml',
        'views/student_progression_achievement_portal.xml',
        'views/assessts.xml',
        'menus/op_menu.xml',
        'report/achievement_progression_report.xml',
    ],
    'images': [
        'static/description/openeducat_achievement_enterprise_banner.jpg',
    ],
    'demo': [
        'demo/achievement_type_demo.xml',
        'demo/achievement_demo.xml',
        'demo/progression_achievement_demo.xml'
    ],
    'qweb': [
        'static/src/xml/ach_widget_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 50,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'live_test_url': 'https://www.openeducat.org/plans'
}
