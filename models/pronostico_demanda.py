# -*- coding: utf-8 -*-
import openpyxl as pyxl
import base64 as base
from odoo import models, fields, api
from tempfile import TemporaryFile
from odoo.exceptions import UserError, ValidationError


class pronostico_demanda(models.Model):
    _name = 'pronostico.demanda'

    name = fields.Char()
    file = fields.Binary(string="Cargar Archivo")
    tipo = fields.Selection([('tipo1','Tipo 1'),('tipo2','Tipo 2')])

    @api.multi
    def read_excel_(self):

        excel_file = base.decodebytes(self.file)
        excel_fileobj = TemporaryFile('wb+')
        excel_fileobj.write(excel_file)
        excel_fileobj.seek(0)
        workbook = pyxl.load_workbook(excel_fileobj,data_only=True)
        sheet = workbook[workbook.get_sheet_names()[0]]

        if self.tipo == 'tipo1':
            for row in sheet.iter_rows(min_row=2):
                vals = {
                    'nombre':row[0].value,
                    'edad' : row[1].value,
                    'sexo' : row[2].value,
                    'codigo' : row[3].value,
                    'file' : self.id
                }
                self.env['datos1'].create(vals)
        elif self.tipo == 'tipo2':
             for row in sheet.iter_rows(min_row=2):
                vals = {
                    'factura': row[0].value,
                    'cliente': row[1].value,
                    'subtotal': row[2].value,
                    'iva': row[3].value,
                    'total' : row[4].value,
                    'file' : self.id
                }
                self.env['datos2'].create(vals)
        else:
            message = 'Message form your friends  \n' + self.error
            raise ValidationError(message)

        return True

    # @api.model
    # def create(self,values):
        # res = super(pronostico_demanda,self).create(values)
        # self.read_excel_()
        # return res

    # @api.model
    # def write(self, values):
        # res = super(pronostico_demanda,self).write(values)
        # self.read_excel_()
        # return res

class Datos1_test(models.Model):
    _name = 'datos1'

    nombre = fields.Char()
    edad = fields.Integer()
    sexo = fields.Char()
    codigo = fields.Integer()
    file = fields.Many2one(comodel_name='pronostico_demanda')

class Datos2_test(models.Model):
    _name = 'datos2'

    factura = fields.Char()
    cliente = fields.Char()
    subtotal = fields.Integer()
    iva = fields.Integer()
    total = fields.Integer()
    file = fields.Many2one(comodel_name='pronostico_demanda')