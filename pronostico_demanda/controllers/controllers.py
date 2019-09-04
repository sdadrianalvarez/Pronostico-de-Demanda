# -*- coding: utf-8 -*-
from odoo import http

# class PronosticoDemanda(http.Controller):
#     @http.route('/pronostico_demanda/pronostico_demanda/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pronostico_demanda/pronostico_demanda/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pronostico_demanda.listing', {
#             'root': '/pronostico_demanda/pronostico_demanda',
#             'objects': http.request.env['pronostico_demanda.pronostico_demanda'].search([]),
#         })

#     @http.route('/pronostico_demanda/pronostico_demanda/objects/<model("pronostico_demanda.pronostico_demanda"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pronostico_demanda.object', {
#             'object': obj
#         })