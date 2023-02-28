from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Visit of Hospital Patients'

    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    visit_date = fields.Date()
    disease_id = fields.Many2one(comodel_name='hr.hospital.disease')
