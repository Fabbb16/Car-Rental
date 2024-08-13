from odoo import http
from odoo.http import request

class WebsitePersonnel(http.Controller):
    @http.route('/personnel', type='http', auth='user', website=True)
    def personnel(self):
        user = request.env.user
        # Check if the user is an admin
        if not user.has_group('base.group_system'):
            return request.redirect('/world')

        personnel = request.env['res.partner'].sudo().search([])
        return request.render('shitesi.partners_template', {'personnel': personnel })


