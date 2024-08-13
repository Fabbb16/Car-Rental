from odoo import http
from odoo.http import request


class OrderController(http.Controller):

    @http.route('/orders/new', type='http', auth='user', website=True)
    def order_form(self, **kw):
        return request.render('shitesi.order_form_template', {})

    @http.route('/orders/create', type='http', auth='public', website=True, csrf=False)
    def create_order(self, **kw):
        # Create the order
        new_order = request.env['wb.order'].sudo().create({
            'car_id': kw.get('car_id'),
            'gift_id': kw.get('gift_id'),
            'order_date': kw.get('order_date'),
            'status': kw.get('status'),
            'contact': kw.get('contact'),
            'con': kw.get('con')
        })

        # Admin's email address (recipient)
        admin_email = 'stafasanifabio2@gmail.com'  # Replace with the actual admin email address

        # Email details for the admin
        mail_values = {
            'subject': 'New Order Created',  # Subject of the email
            'body_html': f"""<p>Dear Admin,</p>
                            <p>A new order has been created. Here are the details:</p>
                           """,  # Body of the email in HTML format
            'email_to': admin_email,  # Recipient's email address
        }

        try:
            mail = request.env['mail.mail'].sudo().create(mail_values)
            mail.send()
            print('Admin Mail Sent')
        except Exception as e:
            print(f'Failed to send email to admin: {str(e)}')

        return request.redirect('/thanks')
