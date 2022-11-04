
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': 'Openeducat Assignment Grading Bridge',
    'version': '14.0.1.0',
    'category': 'Education',
    "sequence": 4,
    'summary': 'Assignment Grading Bridge',
    'complexity': "easy",
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_assignment',
        'openeducat_grading',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/assignment_view.xml',
        'views/gradebook_line_view.xml',
        'views/late_submission_view.xml',
        'views/late_submission_line_view.xml',
        'views/submit_assignment_portal.xml',
        'menus/op_menu.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'live_test_url': 'https://www.openeducat.org/plans'
}
