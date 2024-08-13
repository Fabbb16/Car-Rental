# -*- coding: utf-8 -*-

from odoo import fields, models

class Gifts(models.Model):
    _name = "wb.gift"
    _description = "This is a gift model"

    name = fields.Char(string="Dhurata")
    description = fields.Text(string="Shenim")