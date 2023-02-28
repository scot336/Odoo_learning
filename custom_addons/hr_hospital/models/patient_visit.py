from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Visit of Hospital Patients'

    active = fields.Boolean(default=True)
    doctor_ids = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_ids = fields.Many2one(comodel_name='hr.hospital.patient')
    disease_ids = fields.Many2one(comodel_name='hr.hospital.disease')
    visit_date = fields.Date()
