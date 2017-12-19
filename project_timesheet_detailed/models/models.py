# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class AccountAnalyticLine(models.Model):

    _inherit = 'account.analytic.line'

    stage = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('to review', 'To review'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        default='to review',

    )
    estimated_time = fields.Float('Estimated time', compute='_compute_estimated_time')
    approved_time = fields.Float('Approved time', compute = '_compute_approved_time')

    @api.multi
    @api.depends('task_id')
    def _compute_estimated_time(self):
        for rec in self:
            if rec.task_id:
                rec.estimated_time = rec.task_id.planned_hours

    @api.multi
    @api.depends('task_id')
    def _compute_approved_time(self):
        for rec in self:
            if rec.task_id:
                approved_tms = rec.env['account.analytic.line'].search(
                    [('task_id', '=', rec.task_id.id)]).filtered(
                    lambda rec: rec.stage == 'approved')
                rec.approved_time = sum([tms.unit_amount for tms in approved_tms])

    @api.multi
    def set_approved(self):
        for rec in self:
            rec.write({'stage': 'approved'})

    @api.multi
    def set_rejected(self):
        for rec in self:
            rec.write({'stage': 'rejected'})

    @api.multi
    def set_draft(self):
        for rec in self:
            rec.write({'stage': 'draft'})

    @api.onchange('task_id')
    def task_id_on_change(self):
        if self.task_id:
            self.write({
                'project_id': self.task_id.project_id.id,
                'issue_id': None,
                        })

    @api.onchange('issue_id')
    def issue_id_on_change(self):
        if self.issue_id:
            self.write({
                'issue_id': self.issue_id.project_id.id,
                'task_id': None,
            })

    @api.multi
    def write(self, vals):
        if self.stage == 'rejected':
            vals['stage'] = 'to review'
        return super(AccountAnalyticLine, self).write(vals)

    @api.multi
    def unlink(self):
        for rec in self:
            if rec.stage != 'draft':
                raise UserError('Only records in draft stage can be deleted!')
        return super(AccountAnalyticLine, self).unlink(self)
