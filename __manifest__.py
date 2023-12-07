# -*- coding: utf-8 -*-
{
    'name': "Website Visitor IP",

    'summary': """
        Captures IP Address for Visitors""",

    'description': """
        This Module captures the IP address for every visitor to the website to identify
	 their country and the location of the visitor. 
    """,

    'author': "Mohamed Gad",
    'website': "mohogad@gmail.com",

    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'css': ['static/src/css/styles.css'],
}
