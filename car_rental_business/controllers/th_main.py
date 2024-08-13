from odoo import http
from odoo.http import request


class WebsiteOrder(http.Controller):

    # Get records
    @http.route('/orders', type='http', auth='user', website=True)
    def orders(self, **kw):
        user = request.env.user
        # Check if the user is an admin
        if not user.has_group('base.group_system'):
            return request.redirect('/world')

        orders = request.env['wb.order'].sudo().search([])
        return request.render('shitesi.orders_template', {'orders': orders})







