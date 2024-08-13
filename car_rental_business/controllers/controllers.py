# import json
# from odoo import http
# from odoo.http import request
#
# class GiftController(http.Controller):
#
#     @http.route('/gift', auth='public', csrf=False, type='json', methods=['POST'])
#     def assign_gift(self):
#         api_key = request.httprequest.headers.get('Authorization')
#         if not api_key:
#             return {"success": False, "message": "Duhet celes autorizimi"}
#
#         api_key = api_key.replace('Bearer ', '')
#
#         shites = request.env['wb.shitesi'].sudo().search([('api_key', '=', api_key)], limit=1)
#         if not shites:
#             return {"success": False, "message": "Vetem shitesit mund ta aksesojne kete faqe"}
#
#         try:
#             json_data = json.loads(request.httprequest.data)
#         except json.JSONDecodeError:
#             return {"success": False, "message": "Nuk gjendet te dhena ne Json"}
#
#         buyer_id = json_data.get('buyer_id')
#         gift_id = json_data.get('gift_id')
#
#         if not buyer_id or not gift_id:
#             return {"success": False, "message": "Kujdes buyer_id ose gift_id"}
#
#         Buyer = request.env['wb.buyer'].sudo()
#         Gift = request.env['wb.gift'].sudo()
#
#         buyer = Buyer.search([('id', '=', buyer_id)], limit=1)
#         gift = Gift.search([('id', '=', gift_id)], limit=1)
#
#         if not buyer.exists():
#             return {"success": False, "message": "Bleresi nuk u gjend"}
#
#         if not gift.exists():
#             return {"success": False, "message": "Dhurata nuk u gjend"}
#
#         buyer.gift_id = gift.id  # Directly assign the ID for Many2one field
#
#         buyer_json = {
#             'id': buyer.id,
#             'name': buyer.name,
#             'gift_id': gift.id,
#             'shitesi_name' : shites.name
#         }
#         return {"success": True, "message": "Dhurata iu bashkengjit me sukses", "data": buyer_json}
