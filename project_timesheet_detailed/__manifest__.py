# -*- coding: utf-8 -*-
{
    'name': "project_timesheet_detailed",
    'summary': """This module extends the function of project timesheet, 
    allows the manager to review, approve or reject the timesheet by every 
    single record.""",
    'author': "Elico Corp",
    'website': "https://www.elico-corp.com",
    'category': 'Project Management',
    'version': '10.0.0.1.0',
    'depends': ['project_issue_sheet'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_timesheet_detail_view.xml',
        # 'views/templates.xml',
    ],
    'installable': True,
    'application': False,
}
