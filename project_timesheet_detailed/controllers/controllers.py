# -*- coding: utf-8 -*-
from odoo import http

# class Template(http.Controller):
#     @http.route('/project_timesheet_detailed/project_timesheet_detailed/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_timesheet_detailed/project_timesheet_detailed/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('template.listing', {
#             'root': '/project_timesheet_detailed/project_timesheet_detailed',
#             'objects': http.request.env['project_timesheet_detailed.project_timesheet_detailed'].search([]),
#         })

#     @http.route('/project_timesheet_detailed/project_timesheet_detailed/objects/<model("project_timesheet_detailed.project_timesheet_detailed"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('template.object', {
#             'object': obj
#         })