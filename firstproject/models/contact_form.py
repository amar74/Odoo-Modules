from odoo import models, fields, api

class Contact_form(models.Model):
	_name = 'contact_form'
	name = fields.Char('name')
	lastName = fields.Char('lastname')
	age = fields.Integer('age')
	email = fields.Char('email')
	phone = fields.Char('phone')
	image = fields.Binary('image')

#class statusbar(models.Model):
#	_name = 'statusbar'
#	name = fields.Char('name' required=True)
 #       lastName = fields.Char('name' required=True)
  #      age=fields.Integer('name' required=True)
   #     email=fields.Char('name' required=True)
    #    phone=fields.Integer('name' required=True)
     #   image=fields.Binary('name' required=True)
	state = fields.Selection([
            ('won', 'won'),
            ('new', 'new'),
            ('position', 'position'),
            ('qualified', 'qualified'),
            ],default='won')

	@api.one
	def won(self):
    		self.write({
        		'state': 'won',
    		        	})
	@api.one
	def ne1(self):
    		self.write({
			'state': 'new'
   			 })
	@api.one
	def position(self):
    		self.write({
			'state': 'position'
   			 })
	@api.one
	def qualified(self):
    		self.write({
			'state': 'qualified',
   			 })
