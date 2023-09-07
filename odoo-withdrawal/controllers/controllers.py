# -*- coding: utf-8 -*-
import json
#from odoo import http
#from datetime import datetime

# class WithdrawalController(http.Controller):
#     
#     @http.route('/withdrawal/<string:partner_id>', type='http', auth='user', methods=['POST'], csrf=False)
#     def createReport(self, partner_id, **kw):
#         provider = partner_id
#
#         withdrawal = http.request.env['res.partner.withdrawal'].search(['mail', '=', provider], limit = 1)
#         
#         partner = http.request.env['res.partner'].search(['email', '=', provider], limit = 1)
#         if partner:
#             
             # find products id that has the given email registered as provider
#             supplierInfos = http.request.env['product.supplierinfo'].search(['name', '=', provider])
             
             # find all products linked to the supplierInfos extracted
#             products = []
#             for info in supplierInfos:
#                 products += info.product_tmpl_id
                 #products += http.request.env['product.product'].search(['product_tmpl_id', '=', info.product_tmpl_id])
                 
             # add object as withdrawal object model    
             
#             if not withdrawal:
#                record = Withdrawal()
#                record.products = products
#                record.mail = provider
#                record.partnerId = partner.id
#                record.date = datetime.today()
#                record.status = "in progress"
#                http.request.env['res.partner.withdrawal'].sudo().create(record)
#                withdrawal = record
#             else:
#                 withdrawal.write({
#                     'products': products, 'mail': provider, 'partnerId': partner.id, 'date': datetime.today()
#                 })
#             return http.Response(json.dumps(withdrawal.id), content_type='application/json;charset=utf-8',status=200)    
                     
#        return http.Response(content_type='application/json;charset=utf-8',status=400)