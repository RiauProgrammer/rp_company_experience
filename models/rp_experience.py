# -*- coding: utf-8 -*-

from odoo import models, fields

class Experience(models.Model):
    _name = 'company.experience'
    _description = "Data Experience"

    num_contract = fields.Char(
        string="Contract Number"
    )
    job_name = fields.Char(
        string="Job Name", 
        required=True
    )
    service_user = fields.Char(
        string="Service User", 
        required=True
    )
    scope_service = fields.Text(
        string="Scop of Service", 
        required=True
    )
    periode = fields.Char(
        string="Periode", 
        required=True
    )
    start_date = fields.Date(
        string="Start Date", 
        default=fields.Date.to_string
    )
    end_date = fields.Date(
        string="End Date",
        default=fields.Date.to_string
    )
    price = fields.Float(
        string="Price", 
        required=True
    )
    status = fields.Selection(
        string="Status", 
        selection=[('1','Ongoing'),('2','Pending'),('3','Finish')], 
        required=True
    )
    company_id = fields.Many2one('res.company',
        string="Company", 
        required=True
    )