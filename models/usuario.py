# -*- coding: utf-8 -*-

from odoo import models, fields, api
from cups import require

class usuario(models.Model):
    _name = 'gimnasio.usuario'
    
    nombre = fields.Char('Nombre usuario', size=64, required=True)
    idTarjeta = fields.Char('ID Tarjeta', size=9, required=True)
    foto = fields.Binary('Foto')
    
    clase_ids = fields.Many2many('gimnasio.clase',string='Clases reservadas')