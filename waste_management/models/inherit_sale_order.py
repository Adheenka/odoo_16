# models/sale_order_extension.py

from odoo import models, fields
from odoo.odoo.exceptions import UserError
import base64
import xlsxwriter
from io import BytesIO
from datetime import datetime
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    waste_type = fields.Many2one('product.category', string='Waste Type')
    volume = fields.Char(string='Volume')
    state = fields.Selection(selection_add=[
        ('pickup_scheduled', 'Pickup Scheduled'),
        ('waste_dumped', 'Waste Dumped')
    ])
    driver_id = fields.Many2one('res.partner', string='Driver')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    pickup_point = fields.Char(string='Waste Pickup Point')
    pickup_date = fields.Datetime(string='Pickup Date')
    receiving_id = fields.Many2one('waste.receiving', string='Waste Receiving Facility')
    equipment_id = fields.Many2one('waste.equipment', string='Equipment')

    def action_print_xlsx_report(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        sale_order_ids = data.get('sale_order_ids')

        sale_orders = self.env['sale.order'].browse(sale_order_ids)

        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        sheet = workbook.add_worksheet('Waste Management Report')

        format1 = workbook.add_format({'font_size': 9, 'align': 'vcenter', 'bold': True, 'color': 'gray'})
        date_format = workbook.add_format({'font_size': 9, 'num_format': 'mm/dd/yyyy', 'align': 'vcenter'})
        header_format = workbook.add_format({'font_size': 14, 'align': 'center', 'bold': True, 'color': 'green'})

        sheet.merge_range('C2:O2', 'Waste Management Report', header_format)

        headers = [
            'Date', 'Month', 'Tripsheet No', 'Customer', 'Service Address',
            'Waste Type', 'Volume', 'Driver', 'Vehicle', 'Price', 'Amount', 'VAT',
            'Salesperson', 'Waste Pickup Point'
        ]

        for col, header in enumerate(headers):
            sheet.write(3, col, header, format1)

        row = 4
        for order in sale_orders:
            sheet.write(row, 0, order.date_order.strftime('%Y-%m-%d'), date_format)
            sheet.write(row, 1, order.date_order.strftime('%B'))
            sheet.write(row, 2, order.name)
            sheet.write(row, 3, order.partner_id.name)
            sheet.write(row, 4, order.partner_shipping_id.contact_address)
            sheet.write(row, 5, order.waste_type.name if order.waste_type else '')
            sheet.write(row, 6, order.volume)
            sheet.write(row, 7, order.driver_id.name if order.driver_id else '')
            sheet.write(row, 8, order.vehicle_id.name if order.vehicle_id else '')
            sheet.write(row, 9, order.amount_total)
            sheet.write(row, 10, order.amount_total)
            sheet.write(row, 11, order.amount_tax)
            sheet.write(row, 12, order.user_id.name)
            sheet.write(row, 13, order.pickup_point)
            row += 1

        workbook.close()
        output.seek(0)
        excel_content = output.read()
        excel_base64 = base64.b64encode(excel_content)

        attachment = self.env['ir.attachment'].create({
            'name': 'Waste_Management_Report.xlsx',
            'type': 'binary',
            'datas': excel_base64,
            'res_model': 'sale.order',
            'res_id': sale_orders[0].id,
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % (attachment.id),
            'target': 'self',
        }
    def action_pickup_scheduled(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'pickup.schedule.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
                'default_waste_type': self.waste_type.id,
                # 'default_waste_type': self.waste_type.id if self.waste_type else False,
                'default_volume': self.volume,
                'default_pickup_point':self.pickup_point,
            },
            'name': 'Pickup Scheduled',
        }

    # def action_print_xlsx_report(self, data):
    #     start_date = data.get('start_date')
    #     end_date = data.get('end_date')
    #     sale_order_ids = data.get('sale_order_ids')
    #
    #     sale_orders = self.env['sale.order'].browse(sale_order_ids)
    #
    #     output = BytesIO()
    #     workbook = xlsxwriter.Workbook(output)
    #     sheet = workbook.add_worksheet('Waste Management Report')
    #
    #     format1 = workbook.add_format({'font_size': 9, 'align': 'vcenter', 'bold': True, 'color': 'gray'})
    #     date_format = workbook.add_format({'font_size': 9, 'num_format': 'mm/dd/yyyy', 'align': 'vcenter'})
    #     header_format = workbook.add_format({'font_size': 14, 'align': 'center', 'bold': True, 'color': 'green'})
    #
    #     sheet.merge_range('C2:O2', 'Waste Management Report', header_format)
    #
    #     headers = [
    #         'Date', 'Month', 'Tripsheet No', 'Customer', 'Service Address',
    #         'Waste Type', 'Volume', 'Driver', 'Vehicle', 'Price', 'Amount', 'VAT',
    #         'Salesperson', 'Waste Pickup Point'
    #     ]
    #
    #     for col, header in enumerate(headers):
    #         sheet.write(3, col, header, format1)
    #
    #     row = 4
    #     for order in sale_orders:
    #         sheet.write(row, 0, order.date_order.strftime('%Y-%m-%d'), date_format)
    #         sheet.write(row, 1, order.date_order.strftime('%B'))
    #         sheet.write(row, 2, order.name)
    #         sheet.write(row, 3, order.partner_id.name)
    #         sheet.write(row, 4, order.partner_shipping_id.contact_address)
    #         sheet.write(row, 5, order.waste_type.name if order.waste_type else '')
    #         sheet.write(row, 6, order.volume)
    #         sheet.write(row, 7, order.driver_id.name if order.driver_id else '')
    #         sheet.write(row, 8, order.vehicle_id.name if order.vehicle_id else '')
    #         sheet.write(row, 9, order.amount_total)
    #         sheet.write(row, 10, order.amount_total)
    #         sheet.write(row, 11, order.amount_tax)
    #         sheet.write(row, 12, order.user_id.name)
    #         sheet.write(row, 13, order.pickup_point)
    #         row += 1
    #
    #     workbook.close()
    #     output.seek(0)
    #     excel_content = output.read()
    #     excel_base64 = base64.b64encode(excel_content)
    #
    #     attachment = self.env['ir.attachment'].create({
    #         'name': 'Waste_Management_Report.xlsx',
    #         'type': 'binary',
    #         'datas': excel_base64,
    #         'res_model': 'sale.order',
    #         'res_id': self.id,
    #     })
    #
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': '/web/content/%s?download=true' % (attachment.id),
    #         'target': 'self',
    #     }
    def action_waste_dumped(self):
        self.ensure_one()
        self.write({'state': 'waste_dumped'})






    # def action_print_xlsx_report(self):
    #     output = BytesIO()
    #     workbook = xlsxwriter.Workbook(output)
    #     sheet = workbook.add_worksheet('Waste Management Report')
    #
    #     format1 = workbook.add_format({'font_size': 9, 'align': 'vcenter', 'bold': True, 'color': 'gray'})
    #     date_format = workbook.add_format({'font_size': 9, 'num_format': 'mm/dd/yyyy', 'align': 'vcenter'})
    #     header_format = workbook.add_format({'font_size': 14, 'align': 'center', 'bold': True, 'color': 'green'})
    #
    #     sheet.merge_range('C2:O2', 'Waste Management Report', header_format)
    #
    #     headers = [
    #         'Date', 'Month', 'Tripsheet No', 'Customer', 'Service Address',
    #         'Waste Type', 'Volume', 'Driver', 'Vehicle', 'Price', 'Amount', 'VAT',
    #         'Salesperson', 'Waste Pickup Point'
    #     ]
    #
    #     for col, header in enumerate(headers):
    #         sheet.write(3, col, header, format1)
    #
    #     row = 4
    #     sale_orders = self.env['sale.order'].search([
    #         ('pickup_date', '>=', self.start_date),
    #         ('pickup_date', '<=', self.end_date)
    #     ])
    #     for order in sale_orders:
    #         sheet.write(row, 0, order.date_order.strftime('%Y-%m-%d'), date_format)
    #         sheet.write(row, 1, order.date_order.strftime('%B'))
    #         sheet.write(row, 2, order.name)
    #         sheet.write(row, 3, order.partner_id.name)
    #         sheet.write(row, 4, order.partner_shipping_id.contact_address)
    #         sheet.write(row, 5, order.waste_type.name if order.waste_type else '')
    #         sheet.write(row, 6, order.volume)
    #         sheet.write(row, 7, order.driver_id.name if order.driver_id else '')
    #         sheet.write(row, 8, order.vehicle_id.name if order.vehicle_id else '')
    #         sheet.write(row, 9, order.amount_total)
    #         sheet.write(row, 10, order.amount_total)
    #         sheet.write(row, 11, order.amount_tax)
    #         sheet.write(row, 12, order.user_id.name)
    #         sheet.write(row, 13, order.pickup_point)
    #         row += 1
    #
    #     workbook.close()
    #     output.seek(0)
    #     excel_content = output.read()
    #     excel_base64 = base64.b64encode(excel_content)
    #
    #     attachment = self.env['ir.attachment'].create({
    #         'name': 'Waste_Management_Report.xlsx',
    #         'type': 'binary',
    #         'datas': excel_base64,
    #         'res_model': 'sale.order',
    #         'res_id': self.id,
    #     })
    #
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': '/web/content/%s?download=true' % (attachment.id),
    #         'target': 'self',
    #     }
    #




    # def _prepare_invoice(self):
    #     invoice_vals = super(SaleOrder, self)._prepare_invoice()
    #     # Add custom fields to the invoice if needed
    #     return invoice_vals
    #
    # def action_invoice_create(self):
    #     # Custom logic to handle custom states
    #     if self.state not in ['pickup_scheduled', 'waste_dumped']:
    #         raise UserError("You cannot create an invoice in the current state.")
    #     return super(SaleOrder, self).action_invoice_create()

    # def action_print_xlsx_report(self):
    #     output = BytesIO()
    #     workbook = xlsxwriter.Workbook(output)
    #     sheet = workbook.add_worksheet('Waste Management Report')
    #
    #     format1 = workbook.add_format({'font_size': 9, 'align': 'vcenter', 'bold': True, 'color': 'gray'})
    #     format2 = workbook.add_format({'font_size': 9, 'align': 'vcenter'})
    #     date_format = workbook.add_format({'font_size': 9, 'num_format': 'mm/dd/yyyy', 'align': 'vcenter'})
    #     header_format = workbook.add_format({'font_size': 14, 'align': 'center', 'bold': True, 'color': 'green'})
    #
    #     sheet.merge_range('C2:O2', 'Waste Management Report', header_format)
    #
    #     headers = [
    #         'Date', 'Month', 'Tripsheet No', 'Customer', 'Service Address',
    #         'Waste Type', 'Volume', 'Driver', 'Vehicle', 'Price', 'Amount', 'VAT',
    #         'Salesperson', 'Waste Pickup Point'
    #     ]
    #
    #     for col, header in enumerate(headers):
    #         sheet.write(3, col, header, format1)
    #
    #     row = 4
    #     for order in self:
    #         sheet.write(row, 0, order.date_order, date_format)
    #         sheet.write(row, 1, order.date_order.strftime('%B'))
    #         sheet.write(row, 2, order.name)
    #         sheet.write(row, 3, order.partner_id.name)
    #         sheet.write(row, 4, order.partner_shipping_id.contact_address)
    #         sheet.write(row, 5, order.waste_type.name)
    #         sheet.write(row, 6, order.volume)
    #         sheet.write(row, 7, order.driver_id.name)
    #         sheet.write(row, 8, order.vehicle_id.name)
    #         sheet.write(row, 9, order.amount_total)
    #         sheet.write(row, 10, order.amount_total)
    #         sheet.write(row, 11, order.amount_tax)
    #         sheet.write(row, 12, order.user_id.name)
    #         sheet.write(row, 13, order.pickup_point)
    #         row += 1
    #
    #     workbook.close()
    #     output.seek(0)
    #     excel_content = output.read()
    #     excel_base64 = base64.b64encode(excel_content)
    #
    #     attachment = self.env['ir.attachment'].create({
    #         'name': 'Waste_Management_Report.xlsx',
    #         'type': 'binary',
    #         'datas': excel_base64,
    #         'res_model': 'sale.order',
    #         'res_id': self.id,
    #     })
    #
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': '/web/content/%s?download=true' % (attachment.id),
    #         'target': 'self',
    #     }

    class SaleOrderLine(models.Model):
        _inherit = 'sale.order.line'

        waste_category = fields.Many2one(
            'product.category',
            string='Waste Category',
            related='order_id.waste_type',
            store=True
        )