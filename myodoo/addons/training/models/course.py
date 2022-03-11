from datetime import timedelta
import datetime
from email.policy import default
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)


class TrainingCourse (models.Model):
    _name = "training_course_2" #techncal name
    _description = "second version"
    _order = "id" #way to order instance of this class

    name = fields.Char(string = "name" , required = False , readonly = False , copy = False) 
    active = fields.Boolean(string  = "Active" , default = True)
    start_date = fields.Datetime(string="Stat date") 
    end_date = fields.Datetime(string="end date" , compute = "_get_end_date" , store = True) 
    duration = fields.Integer("Duration")
    course_type = fields.Selection( [ ('online','online'),('onsite','onsite')] , string = "type" , default= "online" )
    resbonsabile_id = fields.Many2one('res.partner',string = "Responsible" ,ondelete = "restrict",
        domain = [('is_company','=',False)]
    )
    # breake relation between this table ..
    # if we have two table .. relation to same table 'res.partner' we should specify 
    # coloumn name of first table and second table 
    attendance_ids = fields.Many2many('res.partner',string= "Attendance" , states={'draft':[('readonly',False)]})
    material_id = fields.Many2one('product.product',string = "Material" ,ondelete = "restrict",
        domain = [('detailed_type','=','service')]
    )
    session_ids = fields.One2many('training_session','course_id',string="Session")
    state = fields.Selection([('draft','draft'),('open','open'),('close','close')] , string = "State" , default= "draft", copy=False)

    course_logo = fields.Image(string = "logo" ,name= "Logo")
    course_file = fields.Binary(string = "File" ,name= "File")

    @api.constrains('start_date','end_date') #save in db
    def checkdate(self):
        if self.start_date and self.end_date:
            if self.end_date<self.start_date:
                raise ValidationError(_("error date"))

    # @api.onchange('start_date','end_date')
    # def validation_date(self):
    #     if self.start_date and self.end_date:
    #         if self.end_date<self.start_date:
    #             raise ValidationError(_("error date"))

    @api.depends('start_date', 'duration')
    def _get_end_date(self): #on tree
        for recorde in self: #self : list of recorde 
            if recorde.start_date and recorde.duration:
                recorde.end_date = recorde.start_date + timedelta(days=recorde.duration)

    def open_course_method(self):
        self.update({'state': 'open' , 'start_date':datetime.datetime.now()})

    def close_course_method(self):
        self.update({'state': 'close'})