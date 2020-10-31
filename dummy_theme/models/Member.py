# -*- coding: utf-8 -*-
##############################################################################
#   ONAERP un fork du projet open source Odoo V12.
#   Copyright (C) 2019 ONA ITConsulting S.P.R.L, (<info@ona-itconsulting.com>).
###############################################################################
###############################################################################

from odoo import api, fields, tools, models, exceptions

class NobleMembers(models.Model):
    _name = "noble.members"
    _description ="Models of subscriber"

    subscriber_name = fields.Char( string="subscriber name",required = True,help="name of subcriber")
    subscriber_first_name = fields.Char( string="subscriber name",required = True,help="first name of subcriber")
    subscriber_born_at = fields.Char( string="subscriber name",required = True,help="subscriber place and date of birth")
    subscriber_mobile_phone = fields.Char( string="subscriber mobile phone",required = True,help="subscriber mobile phone")
    subscriber_professional_phone = fields.Char( string="subscriber professional phone",required = True,help="subscriber professional phone")
    subscriber_email = fields.Char( string="subscriber email",required = True,help="subscriber email")
    subscriber_adress =  fields.Text()

    beneficiary_name = fields.Char(string="beneficiary name", required=True, help="beneficiary name")
    beneficiary_mobile = fields.Char(string="beneficiary mobile", required=True, help="beneficiary mobile")
    beneficiary_mail= fields.Char(string="beneficiary mail", required=True, help="beneficiary mail")
    beneficiary_Address= fields.Char(string="beneficiary address", required=True, help="beneficiary address")
    beneficiary_Remark= fields.Text(string="beneficiary Remark", required=True, help="beneficiary Remark")

    PaiementType = fields.Boolean(string="Type Assurance")
    beneficiary_Reference = fields.Text(string="beneficiary Referenced", required=True, help="beneficiary Referenced")
    organisation_Name = fields.Text(string="organisation name", help="Organisation Name")
    


