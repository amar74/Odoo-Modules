
from odoo import models, fields


class HrAcademic(models.Model):
    _name = 'hr.academic'
    _inherit = 'hr.curriculum'

    diploma = fields.Char('Diploma',
                          translate=True)
    study_field = fields.Char('Field of study',
                              translate=True)
    activities = fields.Text('Activities and associations',
                             translate=True)
