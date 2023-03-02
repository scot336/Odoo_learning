from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(required=True)
    patient_ids = fields.Many2many(comodel_name='hr.hospital.patient')
