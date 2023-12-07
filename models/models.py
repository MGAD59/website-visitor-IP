# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request

class WebsiteVisitorIP(models.Model):
    _inherit = 'website.visitor'
    
    IP_address = fields.Char(compute='_compute_IP', string='IP address')

    @api.depends("IP_address")
    def _compute_IP(self):
        for rec in self:
            client_ip = request.httprequest.environ.get('REMOTE_ADDR', False)
            rec.IP_address = client_ip
            print('hi')
