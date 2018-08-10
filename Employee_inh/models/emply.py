from odoo import models, fields, api
from datetime import date

class Emply(models.Model):
	_name = "hr.employee"
	_inheri = "hr.employee"
	Emname = fields.Char('Name')
	Emphone = fields.Char('Phone no.')
	Ememail = fields.Char('Email ID')
	Emsalary = fields.Integer('Salary')
	Emdate_of_joining = fields.Date('D.O.J')
	Emdocument = fields.Binary('Upload Document')


