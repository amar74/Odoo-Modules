# _*_ coding: utf-8 _*_
from odoo import models, fields

class TodoReport(models.Model):
	_name='todo.tas.report'
	_description='To-do Report'
	_sql="""
		CREATE OR REPLACE VIEW todo_task_report AS
		SELECT * FROM todo_task
		WHERE active = True
	     """
	name = fields.Char('Description')
	is_done = fields.Boolean('Done?')
	active = fields.Boolean('Active?')
	user_id = fields.Many2one('res.users', 'Responsible')
	date_deadline = fields.Date('Deadline')
