from odoo import models, fields,api,_


class movePermitcontract(models.TransientModel):
    _name = 'permit.wizard'


    tenent_name = fields.Many2one('res.partner',string="Tenant’s Name")
    unit_num = fields.Integer(string = "Unit Number")
    rental_payment= fields.Selection([('received', ' Received'),
                                          ('not_received', 'Not received'),
    ],string="Rental Payment")
    security_payment = fields.Selection([('received', ' Received'),
                                          ('not_received', 'Not received'),
                                          ],string="Security Deposit ")
    addc = fields.Selection([('yes', ' Yes'),
                                          ('no', 'No'),
                                          ],string="ADDC Connected ")
    tawtheeq = fields.Selection([('yes', ' Yes'),
                             ('no', 'No'),
                             ], string="Tawtheeq Issued ")
    move_inspection = fields.Selection([('scheduled', 'Scheduled'),
                             ('not_scheduled', 'Not-Scheduled'),
                             ], string="Pre-Move-in Inspection")
    move_date = fields.Date(string="Move In Date")
    parking_slot = fields.Integer(string = "No. of Car Parking Slots")
    car_brand = fields.Char(string = "Brand / Make")
    car_number = fields.Char(string = "Car Plate No.")
    model = fields.Char(string = "Model")
    car_color = fields.Char(string = "Car Color")
    contract_id = fields.Many2one('property.rental',string="contract Id")


    def submit(self):

            self.contract_id.unit_num = self.unit_num
            self.contract_id.rental_payment = self.rental_payment
            self.contract_id.security_payment = self.security_payment
            self.contract_id.addc = self.addc
            self.contract_id.tawtheeq = self.tawtheeq
            self.contract_id.move_inspection = self.move_inspection
            self.contract_id.move_date = self.move_date
            self.contract_id.parking_slot = self.parking_slot
            self.contract_id.car_brand = self.car_brand
            self.contract_id.car_number = self.car_number
            self.contract_id.model = self.model
            self.contract_id.car_color = self.car_color
            self.contract_id.contract_id= self.contract_id
            self.contract_id.created_permit = True



