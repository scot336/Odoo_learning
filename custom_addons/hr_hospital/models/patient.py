from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'

    name = fields.Char(required=True)
    birthday = fields.Date(string="Date of birth")
    doctor_ids = fields.Many2many(comodel_name='hr.hospital.doctor')
    disease_ids = fields.Many2many(comodel_name='hr.hospital.disease')
