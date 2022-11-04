# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

{
    "name": "OpenEducat Dashboard KPI",
    "author": "OpenEduCat Inc",
    "sequence": 10,
    "installable": True,
    "summary": "Beautiful And Responsive Dashboard.",
    "auto_install": False,
    "website": "http://www.openeducat.org",
    "category": "Tools",
    "version": "14.0.1.0",
    "images": [],
    "depends": [
        "base",
        "web",
        "base_setup",
        "openeducat_admission",
        "openeducat_attendance",
        "openeducat_quiz",
        "openeducat_classroom_enterprise",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/dashboard_pro_security.xml",
        "data/default.xml",
        "views/dashboard_pro_theme_view.xml",
        "views/dashboard_pro_view.xml",
        "views/element_view.xml",
        "views/assets_template.xml",
        "menus/menu.xml",
    ],
    "qweb": ["static/src/xml/*.xml"],
    "demo": ["demo/demo.xml", "demo/element_demo.xml"],
    "license": "Other proprietary",
}
