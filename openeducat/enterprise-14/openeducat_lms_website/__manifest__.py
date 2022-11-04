
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': 'OpenEduCat LMS Website',
    'version': '14.0.1.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'LMS',
    'complexity': "easy",
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_lms',
    ],
    'data': [
        'views/assets.xml',
        'views/course_detail_website.xml',
        'views/lms_templates_utils.xml',
        'data/website_data.xml',

    ],
    'demo': [],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 150,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'live_test_url': 'https://www.openeducat.org/plans'
}
