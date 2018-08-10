# _*_ coding: utf-8 _*_
from odoo import models, fields, api
from odoo import exceptions
import logging
_logger = logging.getLogger(__name__)

class TodoWizard(models.TransientModel):
	_name = 'todo.wizard'
	_description = 'To-do Mass Assignment'
	task_ids = fields.Many2many('todo.task', string ='Task')
	new_deadline = fields.Date('Deadline to set')
	new_user_id = fields.Many2one('res.users.',string='Responsible to set')

	@api.multi
	def do_mass_update(self):
		self.ensure_one()
		if not (self.new_deadline or self.new_user_id):
			raise exceptions.ValidationError('No data to update!')
		_logger.debug('Mass update on Todo Task %s', self.task_ids.ids)
		vals = {}
		if self.new_deadline:
			vals['date_deadline'] = self.new_deadline
		if self.new_user_id:
			vals['user_id'] = self.new_user_id
 		# Mass write values on all selected task
		if vals:
			self.task_ids.write(vals)
		return True

	@api.multi
	def _reopen_form(self):
		self.ensure_one()
		return { 'type': 'ir.action.act_window',
			 'res_model': self._name, # This model
			 'res_id': self.id, # This is current wizard model
			 'view_type': 'form',
			 'view_mode': 'form',
			 'target': 'new',
			}
 	@api.multi
	def do_count_tasks(self):
		Task = self.env['todo.task']
		count = Task.search_count([('is done', '=', False)])
		raise exception.Warning( 'There are %d active task.' %count)

	@api.multi
	def do_populate_task(self):
		self.ensure_one()
		Task = self.env['todo.task']
		open_task = Task.search([('is_done', '=', False)])
 	   # fill the wizard task list with all task
		self.task_ids = all_tasks
	   # reopen wizard from on the same wizard record
		return self._reopen_form()

	# Create() structure
	@api.model
	def create(self, vals):
		# code here
		new_record = super(TodoTask, self).create(vals)
		# code after create: can use the new_record created
		return new_record

	# Write() structure
	@api.multi
	def write(self, vals):
		#code before write: can use self, with the old values
		super(TodoTask, self).write(vals)
		# Code after write: can use self, wuth the updated values
		return True
		

