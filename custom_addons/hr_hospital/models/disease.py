from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Disease of Hospital Patient'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    doctor_ids = fields.Many2many(comodel_name='hr.hospital.doctor')
