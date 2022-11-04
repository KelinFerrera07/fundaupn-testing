
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': 'OpenEduCat Backend Theme',
    'category': 'Education',
    'version': '14.0.1.0',
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'summary': 'Backend Theme',
    'depends': [
        'web'
    ],
    'data': [
        'views/assets.xml',
        'views/home.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml'
    ],
    'images': ['static/description/openeducat_backend_theme_banner.jpg'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 100,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'live_test_url': 'https://www.openeducat.org/plans'
}
