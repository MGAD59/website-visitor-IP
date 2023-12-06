# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteVisitorIp(http.Controller):
#     @http.route('/website_visitor__ip/website_visitor__ip', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_visitor__ip/website_visitor__ip/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_visitor__ip.listing', {
#             'root': '/website_visitor__ip/website_visitor__ip',
#             'objects': http.request.env['website_visitor__ip.website_visitor__ip'].search([]),
#         })

#     @http.route('/website_visitor__ip/website_visitor__ip/objects/<model("website_visitor__ip.website_visitor__ip"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_visitor__ip.object', {
#             'object': obj
#         })
