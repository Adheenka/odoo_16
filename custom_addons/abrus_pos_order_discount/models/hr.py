# -*- coding: utf-8 -*-
from odoo import fields, models, api, _

class TableHrEmployeeBase(models.AbstractModel):
	_inherit = "hr.employee.base"

	is_allow_void =fields.Boolean("Allow Void")