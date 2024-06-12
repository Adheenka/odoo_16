from xlsxwriter.utility import xl_rowcol_to_cell

from odoo import models


class ReportBaseWasteManagementXlsx(models.AbstractModel):
    _name = 'report.base_waste_management.report_base_waste_management_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        # Add a new sheet to the workbook
        sheet = workbook.add_worksheet('Waste Management Report')
        bold = workbook.add_format({'bold':True})
        row=3
        col=3
        # Define column headers
        headers = [
            'Pick Up Date',
            'TripSheet Number',
            'Customer',
            'Service Address',
            'Waste Type',
            'Vehicle',
            'Driver',
            'Quantity',
            'Price',
            'VAT 5%',
            'Amount',
            'Waste Receiving Facility'
        ]
        column_widths = [15, 20, 15, 20, 15, 15, 10, 10, 10, 10, 10, 25]
        row_height = 30
        for i, width in enumerate(column_widths):
            sheet.set_column(i + 1, i + 1, width)  # Start columns from index 1
        sheet.set_default_row(row_height)

        # Define a format for the header with a green background
        header_format = workbook.add_format({'bold': True, 'bg_color': '#00FF00'})

        date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})

        start_row = 2
        start_col = 1

        # Write headers to the sheet
        for col, header in enumerate(headers):
            sheet.write(start_row, start_col + col, header, header_format)

        # Write data to the sheet
        row_offset = start_row + 1
        for row, order in enumerate(lines):
            for line in order.order_line:
                sheet.write(row_offset + row, start_col, order.date_order.strftime('%Y-%m-%d'), date_format)
                sheet.write(row_offset + row, start_col + 1, order.name)
                sheet.write(row_offset + row, start_col + 2, order.partner_id.display_name)
                sheet.write(row_offset + row, start_col + 3, order.partner_id.contact_address)
                sheet.write(row_offset + row, start_col + 4, line.product_id.name)
                sheet.write(row_offset + row, start_col + 5, order.vehicle_id.display_name)
                sheet.write(row_offset + row, start_col + 6, order.driver_id.display_name)
                sheet.write(row_offset + row, start_col + 7, line.product_uom_qty)
                sheet.write(row_offset + row, start_col + 8, line.price_unit)
                sheet.write(row_offset + row, start_col + 9, line.price_tax)
                sheet.write(row_offset + row, start_col + 10, line.price_subtotal)
                sheet.write(row_offset + row, start_col + 11, order.receiving_id.display_name)
                row += 1