from odoo import models, fields, api

class WizardSaleOrderReport(models.TransientModel):
    _name = 'wizard.sale.order.report'
    _description = 'Sale Order Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    def action_print_report(self):

        sale_orders = self.env['sale.order'].search([
            ('pickup_date', '>=', self.start_date),
            ('pickup_date', '<=', self.end_date)
        ])

        data = {
            'docs': sale_orders.ids,
        }

        return self.env.ref('base_waste_management.action_report_sale_order_xlsx').report_action(sale_orders)

    # def print_report(self):
    #     self.ensure_one()
    #     [data] = self.read()
    #     data['emp'] = self.env.context.get('active_ids', [])
    #     employees = self.env['hr.employee'].browse(data['emp'])
    #     datas = {
    #         'ids': [],
    #         'model': 'hr.employee',
    #         'form': data
    #     }
    #     return self.env.ref('hr_holidays.action_report_holidayssummary').report_action(employees, data=datas)

