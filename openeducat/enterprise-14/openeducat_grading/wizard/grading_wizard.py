
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

from odoo import models, fields


class GradingWizard(models.TransientModel):
    _name = 'grading.wizard'
    _description = 'Grading Wizard'

    course_id = fields.Many2one('op.course')
    academic_year_id = fields.Many2one('op.academic.year')

    def print_xls_report(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/grading/excel_report/%s' % self.id,
            'target': 'new'
        }
