from odoo import models, fields, api


class prova(models.Model):
     _name = 'prova.prova'
     _description = 'prova_prova'

     name = fields.Char(string='matteo')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100