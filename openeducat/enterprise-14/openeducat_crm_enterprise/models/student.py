
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
##############################################################################

from odoo import models, fields


class OpStudent(models.Model):
    _inherit = "op.student"

    crm_lead_ids = fields.One2many(
        'crm.lead', 'student_id', 'CRM Leads')
