# -*- coding: utf-8 -*-
##############################################################################
#   ONAERP un fork du projet open source Odoo V12.
#   Copyright (C) 2019 ONA ITConsulting S.P.R.L, (<info@ona-itconsulting.com>).
###############################################################################
###############################################################################

from odoo import api, fields, tools, models, exceptions

class Adherants(models.Model):
	_inherit="hr.applicant"
	adresse = fields.Char(string="Adresse")
	postal_code = fields.Char(string="Zip code")
	city_name = fields.Char(string="City name")
	city_of_engage = fields.Char(string="City of choice")
	receive_actuality = fields.Boolean(string="receive actuality") 
	moins_de_35ans = fields.Boolean(string="moins de 35 ans") 

