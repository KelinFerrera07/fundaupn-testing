
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    "name": "Openeducat Attendance Report Xlsx",
    "summary": "Openeducat Attendance Report Xlsx module to create xlsx report",
    "author": "OpenEduCat Inc",
    "website": "http://www.openeducat.org",
    "category": "Education",
    "version": "14.0.1.0.1",
    "license": "Other proprietary",
    "external_dependencies": {"python": ["xlsxwriter", "xlrd"]},
    "depends": ["base", "web"],
    "data": [
        "views/webclient_templates.xml",
        "menu/report.xml"
    ],
    "demo": [],
    "installable": True,
}
