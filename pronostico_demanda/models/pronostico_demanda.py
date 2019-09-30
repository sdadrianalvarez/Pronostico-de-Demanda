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
    tipo = fields.Selection([('mrp','MRP')])

    @api.multi
    def read_excel_(self):

        excel_file = base.decodebytes(self.file)
        excel_fileobj = TemporaryFile('wb+')
        excel_fileobj.write(excel_file)
        excel_fileobj.seek(0)
        workbook = pyxl.load_workbook(excel_fileobj,data_only=True)
        sheet = workbook[workbook.get_sheet_names()[0]]
        if self.tipo == 'mrp':
            for row in sheet.iter_rows(min_row=2):
                vals = {
                    'Articulo': row[0].value,
                    'Descripcion': row[1].value,
                    'Categoria': row[2].value,
                    'Clasificacion': row[3].value,
                    'SubCategoria': row[4].value,
                    'MRPEstatus': row[5].value,
                    'MOQ': row[6].value,
                    'MultiploDeCompra': row[7].value,
                    'LeadTime': row[8].value,
                    'Solicitado': row[9].value,
                    'EnStock': row[10].value,
                    'UltimoProveedor': row[11].value,
                    'UltimoPrecio': row[12].value,
                    'UltimaMoneda': row[13].value,
                    'UltimoPrecioMXP': row[14].value,
                    'UltimaFecha': row[15].value,
                    'CompraReal': row[16].value,
                    'StockTotal': row[17].value,
                    'FechaArribo': row[18].value,
                    'MesDeCobertura': row[19].value,
                    'Mes01': row[20].value,
                    'Mes02': row[21].value,
                    'Mes03': row[22].value,
                    'Mes04': row[23].value,
                    'Mes05': row[24].value,
                    'Mes06': row[25].value,
                    'Mes07': row[26].value,
                    'Mes08': row[27].value,
                    'Mes09': row[28].value,
                    'Mes10': row[29].value,
                    'Mes11': row[30].value,
                    'Mes12': row[31].value,
                    'PuntoDeReorden': row[32].value,
                    'DemandaLT': row[33].value,
                    'DemandaLT2': row[34].value,
                    'StockDeSeguridad': row[35].value,
                    'StockMaximo': row[36].value,
                    'Pedido': row[37].value,
                    'NewMOQ': row[38].value,
                    'LTMeses': row[39].value,
                    'MRPPiezas': row[40].value,
                    'MRPDinero': row[41].value,
                    'UltimaMoneda': row[42].value,
                    'MRPMxp': row[43].value,
                    'MesesSeguridad': row[45].value,
                    'MediaAcotada': row[46].value,
                    'Comprometido': row[47].value,
                    'StockTotalComprometido': row[48].value,
                    'file': self.id
                }
                self.env['mrp'].create(vals)

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

class MRP(models.Model):
    _name = 'mrp'

    Articulo = fields.Char()
    Descripcion = fields.Char()
    Categoria = fields.Char()
    Clasificacion = fields.Char()
    SubCategoria = fields.Char()
    MRPEstatus = fields.Char()
    MOQ = fields.Integer()
    MultiploDeCompra = fields.Integer()
    LeadTime = fields.Integer()
    Solicitado = fields.Integer()
    EnStock = fields.Integer()
    UltimoProveedor = fields.Char()
    UltimoPrecio = fields.Integer()
    UltimaMoneda = fields.Char()
    UltimoPrecioMXP = fields.Integer()
    UltimaFecha = fields.Char()
    CompraReal = fields.Integer()
    StockTotal = fields.Integer()
    FechaArribo = fields.Char()
    MesDeCobertura = fields.Char()
    Mes01 = fields.Integer()
    Mes02 = fields.Integer()
    Mes03 = fields.Integer()
    Mes04 = fields.Integer()
    Mes05 = fields.Integer()
    Mes06 = fields.Integer()
    Mes07 = fields.Integer()
    Mes08 = fields.Integer()
    Mes09 = fields.Integer()
    Mes10 = fields.Integer()
    Mes11 = fields.Integer()
    Mes12 = fields.Integer()
    PuntoDeReorden = fields.Integer()
    DemandaLT = fields.Integer()
    DemandaLT2 = fields.Integer()
    StockDeSeguridad = fields.Integer()
    StockMaximo = fields.Integer()
    Pedido = fields.Integer()
    NewMOQ = fields.Integer()
    LTMeses = fields.Integer()
    MRPPiezas = fields.Integer()
    MRPDinero = fields.Integer()
    UltimaMoneda = fields.Char()
    MRPMxp = fields.Integer()
    MesesSeguridad = fields.Integer()
    MediaAcotada = fields.Integer()
    Comprometido = fields.Integer()
    StockTotalComprometido = fields.Integer()
    file = fields.Many2one(comodel_name='pronostico_demanda')

class Datos2_test(models.Model):
    _name = 'datos2'

    factura = fields.Char()
    cliente = fields.Char()
    subtotal = fields.Integer()
    iva = fields.Integer()
    total = fields.Integer()
    file = fields.Many2one(comodel_name='pronostico_demanda')