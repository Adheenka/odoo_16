# -*- coding: utf-8 -*-
""" explication """

from odoo import models, fields, api


class OdooTodoList(models.Model):
    """ explication """
    _name = 'odoo.todo.list'
    _description = 'OWL Todo list App'

    name = fields.Char(string="Task name")
    completed = fields.Boolean()
    color = fields.Char()

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name must be unique !')
    ]


