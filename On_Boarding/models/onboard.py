from odoo import models, fields, api
from datetime import date
import re
from odoo.exceptions import ValidationError
class employee_form(models.Model):
        _name="onboard.employee"
	name = fields.Char('Name')
	position = fields.Many2one('hr.job', string='Position')
	department = fields.Many2one('hr.department', string='Department')
	parent = fields.Many2one('hr.employee', string='Manager')
	doj = fields.Date('Date of Joining')
	salary = fields.Integer('Salary')
	email = fields.Char('Personal Email ID')
	phone = fields.Char('Mobile No.')
	
	#value_pass = fields.Boolean(string='Has passed our super method')
	
        def submit(self, values):
		self.env['hr.employee'].create(
			               {
					'name': self.name, 
					'job_id': self.position,				
					#'department_id': self.department,
					#'parent_id': self.parent,
					'work_email': self.email,
					'work_phone': self.phone,
					'Emsalary': self.salary,
					'DOJ': self.doj	
					})
						

	

	@api.onchange('phone')
	def valid_phone(self):
    		if self.phone:
			if not(re.match(r'(^[+0-9]{1,3})*([0-9]{10,11}$)', self.phone)):
				raise ValidationError("Please Enter Valid Phone no.")

	@api.onchange('email')
	def validate_mail(self):
		if self.email:
			if not(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)):
				raise ValidationError('Enter valid E-mail ID')

	

