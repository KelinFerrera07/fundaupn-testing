# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': "OpenEduCat Secure",
    'version': '14.0',
    'depends': ['web', 'base', 'openeducat_core_enterprise'],
    'author': 'OpenEduCat Inc',
    'website': 'http://www.openeducat.org',
    'data': [
        'security/ir.model.access.csv',
        'data/parameter_data.xml',
        'views/secure.xml',
        'views/assets.xml',
        'views/res_config_setting_view.xml',
        'views/error_page.xml',
        'views/qr_code_verify.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 99,
    'currency': 'EUR',
    'license': 'Other proprietary',
}
