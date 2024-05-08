from odoo import models, fields, api


class room__app(models.Model):
    _name = 'room__app.room__app'
    _description = 'room__app.room__app'

    status = fields.Boolean(string='Status')
    name = fields.Char(string='Room Name', required=True)
    short_name = fields.Char(string='Short Name')
    photos = fields.Binary(string='Photos')
    main_places = fields.Integer(string='Main Places')
    additional_places = fields.Integer(string='Additional Places')
    room_type = fields.Selection([
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
        ('villa', 'Villa'),
        ('other', 'Other')], string='Room Type', default='standard', required=True)

    def action_edit_room(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'room__app.room__app',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'target': 'current',
            'flags': {'form': {'action_buttons': True}},
        }

    def action_copy_room(self):
        copied_room = self.copy()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'room__app.room__app',
            'view_mode': 'form',
            'target': 'current',
            'res_id': copied_room.id,
        }

    def action_delete_room(self):
        self.unlink()
        return {'type': 'ir.actions.act_window_close'}


    def action_copy_room_link(self):
        room_link = f"/your_custom_route/{self.id}"

        return {
            'name': 'Room Link',
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Room Link',
                'message': f'Copy this link: <a href="{room_link}" target="_blank">{room_link}</a>',
                'sticky': False,
            }
        }


class room_availability(models.Model):
    _name = 'room__app.room_availability'
    _description = 'room__app.room_availability'

    room_id = fields.Many2one('room__app.room__app', string='Room', required=True)
    date = fields.Date(string='Date', required=True)
    is_available = fields.Boolean(string='Is Available', default=True)
    notes = fields.Text(string='Notes')
