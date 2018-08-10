from odoo import models, fields, api
 
class res_partner(models.Model):
	_inherit = 'res.partner'
	@api.multi
	def send_mail(self):
                mail = self.env.ref('mail_form.mail_send')
                self.env['mail_send'].browse(mail.id).send_mail(self.id)
