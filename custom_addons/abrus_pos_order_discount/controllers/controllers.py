# -*- coding: utf-8 -*-
# from odoo import http


# class AbrusPosBom(http.Controller):
#     @http.route('/abrus_pos_bom/abrus_pos_bom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abrus_pos_bom/abrus_pos_bom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('abrus_pos_bom.listing', {
#             'root': '/abrus_pos_bom/abrus_pos_bom',
#             'objects': http.request.env['abrus_pos_bom.abrus_pos_bom'].search([]),
#         })

#     @http.route('/abrus_pos_bom/abrus_pos_bom/objects/<model("abrus_pos_bom.abrus_pos_bom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abrus_pos_bom.object', {
#             'object': obj
#         })
