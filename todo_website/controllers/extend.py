# _*_ coding: utf-8 _*_
from odoo import http
from odoo.addons.todo_website.controllers.main import Todo

class TodoExtended(Todo):
	@http.route()
	def hello(self, name=None, **kwargs):
		response = super(TodoExtended, self).hello()
		response.qcontext['name'] = name
		return response
