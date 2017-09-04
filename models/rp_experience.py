# -*- coding: utf-8 -*-

from odoo import models, fields

class Experience(models.Model):
    _name = 'company.experience'
    _description = "Data Experience"
    _inherit = ['mail.thread']

    num_contract = fields.Char(
        string="Contract Number", 
        track_visibility='onchange'
    )
    job_name = fields.Char(
        string="Job Name", 
        required=True, 
        track_visibility='onchange'
    )
    partner_id = fields.Many2one('res.partner',
        string="Customer", 
        required=True, 
        track_visibility='onchange'
    )
    scope = fields.Text(
        string="Scop of Service", 
        required=True, 
        track_visibility='onchange'
    )
    periode = fields.Char(
        string="Periode", 
        required=True, 
        track_visibility='onchange'
    )
    start_date = fields.Date(
        string="Start Date", 
        default=fields.Date.to_string, 
        track_visibility='onchange'
    )
    end_date = fields.Date(
        string="End Date",
        default=fields.Date.to_string, 
        track_visibility='onchange'
    )
    price = fields.Float(
        string="Price", 
        required=True, 
        track_visibility='onchange'
    )
    status = fields.Selection(
        string="Status", 
        selection=[('1','Ongoing'),('2','Pending'),('3','Finish')], 
        required=True, 
        track_visibility='onchange'
    )
    company_id = fields.Many2one('res.company',
        string="Company", 
        required=True, 
        track_visibility='onchange'
    )

    color = fields.Integer()