
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    'name': 'OpenEduCat Fees On Sesion',
    'version': '14.0.1.0',
    'license': 'Other proprietary',
    'depends': ['openeducat_attendance_enterprise',
                'openeducat_fees_enterprise',
                'openeducat_admission_enterprise'],
    'data': [
        'security/ir.model.access.csv',
        'views/fees_session_based_view.xml'
    ],
    'demo': [
        'demo/product_demo.xml',
        'demo/fees_element_line_demo.xml',
        'demo/fees_terms_line_demo.xml',
        'demo/fees_terms_demo.xml',
        'demo/faculty_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
