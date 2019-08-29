# -*- coding: utf-8 -*-
import pandas as pnd
import base64 as base
from odoo import models, fields, api
from tempfile import TemporaryFile

class pronostico_demanda(models.Model):
    _name = 'pronostico.demanda'

    name = fields.Char()
    file = fields.Binary(string="Cargar Archivo")


    @api.multi
    def read_excel_(self):

        excel_file = base.decodebytes(self.file)
        excel_fileobj = TemporaryFile('wb+')
        excel_fileobj.write(excel_file)
        excel_fileobj.seek(0)
        res =  pnd.read_excel(excel_fileobj)
        
        return res

    @api.model
    def create(self,values):
        res = super(pronostico_demanda,self).create(values)
        return res