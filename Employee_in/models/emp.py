from odoo import fields, models, api
class Employee(models.Model):
	_name = 'hr.employee'
	_inherit = ['hr.employee']
	Emname = fields.Char('Partner Name')
        Emphone = fields.Char('Phone no.')
        Ememail = fields.Char('Email ID')
        Emsalary = fields.Integer('Salary')
        DOJ = fields.Date(string="DOJ")
	Emdocument = fields.Binary('Upload Document')
	crmamar = fields.Many2one('crm.lead', string='CRM Pipeline')
        date = fields.Many2one('crm.lead', string='Pipeline')
        date_deadline = fields.Date(related='date.date_deadline', string="Closing Date")
	planned = fields.Many2one('crm.lead', string='Revenue')
	planned_revenue = fields.Float(related='planned.planned_revenue', string='Expected Revenue')
	prob = fields.Many2one('crm.lead', string='Address')
	probability = fields.Float(related='prob.probability', string='Probability')
	#def submit(self):
	#	self.writ({})

