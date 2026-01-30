from odoo import models, fields

class lib_book(models.Model):
    _name = "lib.book"
    _description = "Book Management"

    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author")
    description = fields.Text(string="Description")
    publication_date = fields.Date(string="Publication Date")
    price = fields.Float(string="Price")
    status = fields.Boolean(string="Available")
