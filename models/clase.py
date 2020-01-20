# -*- coding: utf-8 -*-

from odoo import models, fields, api
from cups import require

class clase(models.Model):
    _name = 'gimnasio.clase'
    
    nombre = fields.Char('Clase', size=64, required=True)
    inicio = fields.Datetime('Inicio', required=True, autodate=True)
    fin = fields.Datetime('Fin', required=True, autodate=True)
    capacidad = fields.Integer("Capacidad")
    tipoActividad = fields.Selection([('baile','Baile'),
                                      ('aerobic','Aerobic'),
                                      ('anaerobic','Anaerobic'),
                                      ('relax','Relax'),],
                                     'Tipo de Actividad')
    
    # OJO! El primer parámetro es el _name del otro modelo
    usuario_ids = fields.Many2many('gimnasio.usuario',string='Usuarios Confirmados')

# class gimnasio(models.Model):
#     _name = 'gimnasio.gimnasio'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100