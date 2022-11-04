
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': 'OpenEduCat Fees On Duration',
    'version': '14.0.1.0',
    'license': 'Other proprietary',
    'depends': ['openeducat_fees_enterprise',
                'openeducat_core_enterprise'],
    'data': [
        'views/fees_duration_based_view.xml'
    ],
    'demo': [
        'demo/product_demo.xml',
        'demo/fees_element_line_demo.xml',
        'demo/fees_terms_line_demo.xml',
        'demo/fees_terms_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
