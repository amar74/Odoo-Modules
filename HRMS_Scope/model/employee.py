from odoo import models, fields, api

class employee_form(models.Model):
	_name = 'employee_form'
	_inherit = 'hr.employee'
        name = fields.Char('Name', required=True)
        email = fields.Char('Email', required=True)
        #phone = fields.Char('phone', required=True)
	position = fields.Char('Position')
	department = fields.Char('Department', required=True)
	reporting_manager = fields.Char('Reporting Manager')
	date_of_join = fields.Char('Date of Join', required=True)
	salary = fields.Integer('Salary', required=True)
	name1 = fields.Char('Name')
	DOJ = fields.Char('DOJ')
	degination = fields.Char('Degination')
	street1 = fields.Char('Street')
	city1 = fields.Char('City')
	state_id1 = fields.Char('State')
	zip_id1 = fields.Integer('ZIP Code')
	country_id1 = fields.Char('Countary')
	Non_disclosure_agreement = fields.Binary('Non disclosure agreement')
	emname = fields.Char('Name')
	emDOJ = fields.Char('DOJ')
	emdegination = fields.Char('Degination')
	ctc = fields.Char('CTC')
	Employee_agreement = fields.Binary('Employee Agreement')
	street = fields.Char('Street')
	city = fields.Char('City')
	state_id = fields.Char('State')
	zip_id = fields.Integer('ZIP Code')
	country_id = fields.Char('Countary')
	anti_Sexual = fields.Binary('Anti-Sexual Harssment policy')
	Ethics_policy = fields.Binary('Ethic Policy')
	ESOPs = fields.Binary('ESOPs if-any ')
	PF_form = fields.Binary('PF Form 11, Form 2')
	Gratuity_form = fields.Binary('Gratuity Form')
	mac = fields.Boolean('Macbook')
	Laptop = fields.Boolean('Laptop')
	Desktop = fields.Boolean('Desktop')
	Thinkpad = fields.Boolean('Thinkpad')
	sim = fields.Boolean('Sim Card')
	bussiness = fields.Boolean('Bussiness Card')
	parking = fields.Boolean('Parking')
	
        def hired(self):
                self.write({})
	#Hired Buuton	
	#@api.one
	#def Hired(self):
	#	hired = self.env['employee_form'].sudo().search([('name','=','Hired')], limit=1)
	#	body = hired.body_html
		#body=body.replace('--name--',self.name.Name)
		#body=body.replace('--email--',self.email.Email)
		#body=body.replace('--position--',self.position.Position)
		#body=body.replace('--department--',self.department.Department)
		#body=body.replace('--reporting_manager--',self.reporting_manager.Reparting_Manager)
		#body=body.replace('--doj--',date_of_join.DOJ)
		#body=body.replace('--salary--',salary.Salary)
		#if hired:
			#mail_values = {
			#'subject': hired.subject,
			#'body_html': body,
			#'email_to':';'.join(map(lambda x: x, receipt_list)),
			#'email_cc':';'.join(map(lambda x: x, email_cc)),
			#'email_from': template_obj.email_from,}
			#create_and_send_email = self.env['mail.mail'].create(mail_values).send()       
 
