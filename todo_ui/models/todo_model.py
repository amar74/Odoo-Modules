#  __*__ coding utf-8 __*__
from odoo import models, fields, api
from odoo.exceptions import ValidationError
class Tag(models.Model):
	_name = 'todo.task.tag'
	_description = 'To-do Tag'
	_parent_store = True
   # _parent_name = 'parent_id'
	name= fields.Char('Name')
	parent_id = fields.Many2one('todo.tassk.tag', 'Parent Tag', ondelete='restrict')
	parent_left = fields.Integer('Parent Left', index=True)
	parent_right = fields.Integer('Parent Right', index=True)
	child_ids = fields.One2many('todo.task.tag', 'parent_id', 'Child Tags')
class Stage(models.Model):
	_name = 'todo.task.stage'
	_description = 'To-do Stages'
	_order = 'sequence,name'
    # String fields
	name = fields.Char('Name',size=40)
 	desc = fields.Text('Description')
	state = fields.Selection([('draft','New'),('open','Started'),('done','Closed')],'State')
	docs = fields.Html('Documentation')
    # Numeric Fields
	sequence = fields.Integer('Sequence')
	perc_complete = fields.Float('% Complete', (3, 2))
    # Date Fields
	date_effctive = fields.Date('Effective Date')
	date_changed = fields.Datetime('Last changed')

    # Other fields
	fold = fields.Boolean('Folded?')
	image = fields.Binary('Image')
class TodoTask(models.Model):
	_inherit = 'todo.task'
	stage_id = fields.Many2one('todo.task.stage', 'Stage')
	tag_ids = fields.Many2many('todo.task.tag', string='Tags')
	stage_fold = fields.Boolean('Stage Folded?', compute='_compute_stage_fold')
	stage_state = fields.Selection(related='stage_id.state', string='Stage State')
	_sql_contraints = [('todo_task_name_uniq', 'UNIQUE (name, active)', 'Task title must be unique!')]
	refers_to = fields.Char('Referes To')
	state = fields.Selection (related='stage_id.state', string='Stage State')
	my_image = fields.Binary('Image')
	effort_estimate = fields.Integer('Effort Estimate')
		

	@api.depends('stage_id.fold')
	def _compute_stage_fold(self):
		for task in self:
			task.stage_fold = task.stage_id.fold
	@api.constrains('name')
	def _check_name_size(self):
		for todo in self:
			if len(todo.name) < 5:
				raise ValidationError('Must have 5 chars!')
	def compute_user_todo_count(self):
		for task in self:
			task.user_todo_count = task.search_count([('user_id', '=', task.user_id.id)])
	user_todo_count = fields.Integer('User To-Do Count', compute='compute_user_todo_count')
