from odoo import models, fields, api
from odoo16E.odoo.exceptions import UserError


class WizardSaleOrderReport(models.TransientModel):
    _name = 'wizard.sale.order.report'
    _description = 'Sale Order Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    # def action_print_report(self):
    #
    #     sale_orders = self.env['sale.order'].search([
    #         ('pickup_date', '>=', self.start_date),
    #         ('pickup_date', '<=', self.end_date)
    #     ])
    #
    #     data = {
    #         'docs': sale_orders.ids,
    #     }
    #
    #     return self.env.ref('waste_management.action_print_xlsx_report').report_action(sale_orders)

    # def action_print_report(self):
    #     sale_orders = self.env['sale.order'].search([
    #         ('pickup_date', '>=', self.start_date),
    #         ('pickup_date', '<=', self.end_date)
    #     ])
    #     return sale_orders.action_print_xlsx_report()

    # def action_print_report(self):
    #     sale_orders = self.env['sale.order'].search([
    #         ('pickup_date', '>=', self.start_date),
    #         ('pickup_date', '<=', self.end_date)
    #     ])
    #
    #     data = {
    #         'sale_order_ids': sale_orders.ids,
    #         'start_date': self.start_date,
    #         'end_date': self.end_date
    #     }
    #
    #     return sale_orders.action_print_xlsx_report(data)

    def action_print_report(self):
        sale_orders = self.env['sale.order'].search([
            ('pickup_date', '>=', self.start_date),
            ('pickup_date', '<=', self.end_date)
        ])

        data = {
            'sale_order_ids': sale_orders.ids,
            'start_date': self.start_date,
            'end_date': self.end_date
        }

        if sale_orders:
            return sale_orders[0].action_print_xlsx_report(data)

        return {
            'type': 'ir.actions.act_window_close'
        }