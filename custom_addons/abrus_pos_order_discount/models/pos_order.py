# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, AccessError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class PosOrderLineInherit(models.Model):
	_inherit = 'pos.order.line'

	discount_remark = fields.Char('Discount Remark')
	discount_for = fields.Selection([('wastage','Wastage'),('no_make','No Make')])

class VoidPOSSession(models.Model):
	_inherit = 'pos.session'

	def _loader_params_hr_employee(self):
		result = super()._loader_params_hr_employee()
		result['search_params']['fields'].extend(['is_allow_void'])
		return result
