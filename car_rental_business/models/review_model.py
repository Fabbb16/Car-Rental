# -- coding: utf-8 --

from odoo import fields, models

class Review(models.Model):
    _name = "wb.review"
    _description = "This is a review model"

    # buyer_id = fields.Many2one("wb.buyer", string="Bleresi")
    contact = fields.Many2one('res.partner', string="Bleresi")
    car_id = fields.Many2one("fleet.vehicle", string="Makina e blere")
    rating = fields.Selection([
        ('1⭐', '1⭐'),
        ('2⭐', '2⭐'),
        ('3⭐', '3⭐'),
        ('4⭐', '4⭐'),
        ('5⭐', '5⭐')
    ], string="Vleresimi")
    comment = fields.Text(string="Komenti")