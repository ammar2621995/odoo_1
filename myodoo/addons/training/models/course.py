from email.policy import default
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)


class TrainingCourse (models.Model):
    _name = "training_course_2" #techncal name
    _description = "second version"
    _order = "id" #way to order instance of this class

    name = fields.Char(string = "name" , required = True , readonly = True , copy = False) 
    active = fields.Boolean(string  = "Active" , default = True)
    start_date = fields.Datetime(string="Stat date") 
    end_date = fields.Datetime(string="end date") 
    duration = fields.Integer("Duration")