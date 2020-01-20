# -*- coding: utf-8 -*-

from odoo import models, fields, api
from cups import require

class profesor(models.Model):
    _name = 'gimnasio.profesor'
    
    nombre = fields.Char('Nombre profesor', size=64, required=True)
    idTarjeta = fields.Char('ID Tarjeta', size=9, required=True)
    foto = fields.Binary('Foto')