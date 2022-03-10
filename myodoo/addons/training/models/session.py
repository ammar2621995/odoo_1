from email.policy import default
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)


class CourseSession (models.Model):
    _name = "training_session" #techncal name
    _description = "second version"
    _order = "id" #way to order instance of this class

    name = fields.Char(string= "Name" , readonly = False , copy = False)
    content = fields.Text("Content")
    planned_date = fields.Datetime(string = "Planned Date")
    actual_date  = fields.Datetime(string = "Actual Date" , readonly = True)
    course_id = fields.Many2one('training_course_2',string="Course")