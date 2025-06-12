import requests
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SendcloudAPI(models.Model):
    _name = 'sendcloud.api'
    _description = 'Sendcloud API Connector'

    name = fields.Char(string='Connection Name', required=True)
    public_key = fields.Char(string='Public Key', required=True)
    secret_key = fields.Char(string='Secret Key', required=True)

    def _get_headers(self):
        return {
            'Content-Type': 'application/json'
        }

    def _get_auth(self):
        return (self.public_key, self.secret_key)

    def fetch_parcels(self):
        url = "https://panel.sendcloud.sc/api/v2/parcels"
        response = requests.get(url, headers=self._get_headers(), auth=self._get_auth())

        if response.status_code == 200:
            return response.json().get('parcels', [])
        else:
            raise UserError(_('Failed to fetch parcels: %s') % response.text)
