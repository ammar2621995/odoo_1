from email.policy import default
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)


class TrainingCourse (models.Model):
    _name = "training_course_2" #techncal name
    _description = "second version"
    _order = "id" #way to order instance of this class

    name = fields.Char(string = "name" , required = True , readonly = False , copy = False) 
    active = fields.Boolean(string  = "Active" , default = True)
    start_date = fields.Datetime(string="Stat date") 
    end_date = fields.Datetime(string="end date") 
    duration = fields.Integer("Duration")
    course_type = fields.Selection( [ ('online','online'),('onsite','onsite')] , string = "type" , default= "online" )


    @api.constrains('start_date','end_date')
    def checkdate(self):
        if self.start_date and self.end_date:
            if self.end_date<self.start_date:
                raise ValidationError(_("error date"))

    # @api.onchange('start_date','end_date')
    # def validation_date(self):
    #     if self.start_date and self.end_date:
    #         if self.end_date<self.start_date:
    #             raise ValidationError(_("error date"))