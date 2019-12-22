# -*- coding: utf-8 -*-

from odoo import models,fields


class StudentInfo(models.Model):
    _name = 'student.state'

    name = fields.Char(string = "Name", required="true")
    city_ids = fields.One2many('student.city', 'state_id')

class StudentInfo(models.Model):
    _name = 'student.city'

    name = fields.Char(string = "Name", required="true")
    state_id = fields.Many2one('student.state')



class StudentInfo(models.Model):
    _name = 'student.info'

    name = fields.Char(string = "Name")
    work_info = fields.Char(string="Work Info")
    city =  fields.Many2one('student.city')
    state = fields.Many2one('student.state')
    pincode = fields.Integer(size=6)
    phone_no = fields.Integer(size=10)
    location = fields.Text()
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string='Gender')
    date_of_birth = fields.Date(string="Date Of Birth")
    marital_status = fields.Selection([('single', 'Single'),('married', 'Married')], string='Marital Status')
    passport_no = fields.Char()
    badge_id = fields.Char(string = "Badge Id")
    manay_attendance = fields.Boolean()
    relate_user = fields.Many2one('res.users')
    address = fields.Char()
    age = fields.Integer(size=3)











