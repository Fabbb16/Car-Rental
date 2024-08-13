from odoo import http
from odoo.http import request

class WebsiteGifts(http.Controller):
    @http.route('/gifts', auth='user', type='http', website=True)
    def gifts(self):
        gifts = request.env['wb.gift'].sudo().search([])
        return request.render('shitesi.gifts_template', {'gifts': gifts})