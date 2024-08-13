# -*- coding: utf-8 -*-

from odoo import fields, models

class Orders(models.Model):
    _name = 'wb.order'
    _description = 'This is an order model'

    car_id = fields.Many2one("fleet.vehicle", string="Makina e blere")
    gift_id = fields.Many2one("wb.gift", string="Dhurata e marre")
    order_date = fields.Date(string="Data e porosises")
    status = fields.Selection([('completed', 'Completed'), ('pending', 'Pending')])
    contact = fields.Many2one('res.partner', string="Shitesi")
    con = fields.Many2one('res.partner', string="Bleresi")


