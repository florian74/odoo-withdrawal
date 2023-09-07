# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api
from datetime import datetime

_logger = logging.getLogger(__name__)


class WithdrawalConfig(models.TransientModel):
    _inherit = 'res.config.settings'
    contribution = fields.Float(string="Retained Contribution (%)",
                                default=10.0,
                                config_parameter='odoo-withdrawal.contribution')

    def set_values(self):
        super().set_values()
        self.env['ir.config_parameter'].set_param('odoo-withdrawal.contribution', self.contribution)


class Withdrawal(models.Model):
    _name = 'res.partner.withdrawal'
    _description = 'withdrawal generated report'

    partner_id = fields.Many2one('res.partner', 'Owner')
    date = fields.Datetime(string="Date withdrawal")
    name = fields.Char('Name')

    mail = fields.Char('Mail')
    products = fields.One2many('product.template', 'id', store=False, compute='_compute_products')

    currency_id = currency_id = fields.Many2one("res.currency", readonly=True, default=lambda self: self.env.company.currency_id)

    gain = fields.Monetary('Gain', default=0.0, currency_field="currency_id")
    fees = fields.Monetary('Fees', default=0.0, currency_field="currency_id")
    total = fields.Monetary('Total', default=0.0, currency_field="currency_id")

    @api.depends('partner_id')
    def _compute_products(self):
        self.products = []
        if self.partner_id:
            self.date = datetime.today()
            _logger.info('recompute product list')
            _logger.info(self.partner_id)
            _logger.info(self.partner_id.email)
            _logger.info(self.partner_id.id)
            if self.partner_id:
                _logger.info('partner found')
                self.mail = self.partner_id.email
                self.name = self.partner_id.name
                targetId = self.partner_id.id
                # find products id that has the given email registered as provider
                supplierInfos = self.env['product.supplierinfo'].search([('partner_id', '=', targetId)])

                # find all products linked to the supplierInfos extracted + compute total HT
                products = []
                self.gain = 0.0
                self.total = 0.0
                self.fees = 0.0
                self.currency_id = self.env.company.currency_id
                for info in supplierInfos:
                    _logger.info('new product found')
                    _logger.info(info.product_id)
                    _logger.info(info.product_id.id)
                    _logger.info(info.product_tmpl_id)
                    _logger.info(info.product_tmpl_id.id)
                    if info.product_tmpl_id.id:
                        products.append(info.product_tmpl_id.id)
                        self.gain = self.gain + info.product_tmpl_id.list_price * info.product_tmpl_id.sales_count
                    elif info.product_id.id:
                        related_template = self.env['product.product'].search([('id', '=', info.product_id.id)],
                                                                              limit=1)
                        if related_template.product_tmpl_id.id:
                            products.append(related_template.product_tmpl_id.id)
                            self.gain = self.gain + related_template.product_tmpl_id.list_price * related_template.product_tmpl_id.sales_count
                    _logger.info(products)

                # load contribution settings
                contribution = self.env['ir.config_parameter'].sudo().get_param('odoo-withdrawal.contribution')
                self.fees = self.gain * float(contribution) / 100.0
                self.total = self.gain - self.fees

                # add object as withdrawal object model
                self.products = products

    def create_report(self):
        if not self.partner_id.id:
            return
        return self.env.ref('odoo-withdrawal.action_withdrawal_pdf_report').report_action(self)