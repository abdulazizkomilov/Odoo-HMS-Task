# -*- coding: utf-8 -*-
# from odoo import http


# class RoomApp(http.Controller):
#     @http.route('/room__app/room__app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/room__app/room__app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('room__app.listing', {
#             'root': '/room__app/room__app',
#             'objects': http.request.env['room__app.room__app'].search([]),
#         })

#     @http.route('/room__app/room__app/objects/<model("room__app.room__app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('room__app.object', {
#             'object': obj
#         })

