from odoo import http
from odoo.http import request


class WebsiteFleet(http.Controller):
    @http.route('/fleet', type='http', auth='user', website=True)
    def fleet(self):
        fleets = request.env['fleet.vehicle'].sudo().search([])
        return request.render('shitesi.fleet_list_template', {"fleets": fleets})