# -*- coding: utf-8 -*-
"""
.. module:: icon
   :platform: Unix, Windows
   :synopsis: Operator application tray icon behavior

.. moduleauthor:: Anton Konyshev <anton.konyshev@gmail.com>

"""

import wx

from config import CONFIG
from utils import img
import ids
import events as ev


class OperIcon(wx.TaskBarIcon):
    """Tray icon"""

    def event_table(self):
        """Tray icon event table"""
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.on_main_action)
        self.Bind(wx.EVT_TASKBAR_RIGHT_DOWN, self.on_actions_list)
        self.Bind(wx.EVT_MENU, self.on_menu_item)
        self.Bind(ev.PRESENCE_UPDATED_EVENT, self.on_presence_updated)

    def __init__(self, app, *args, **kwargs):
        """Application tray icon init"""
        super(OperIcon, self).__init__(*args, **kwargs)
        self.app = app
        self.presence = 'offline'
        self.event_table()

    def on_presence_updated(self, e):
        """Updates an information about the presence status"""
        self.presence = e.presence if e.presence is not None else 'online'

    def popup_menu(self):
        """Creates and returns tray icon popup menu"""
        status_menu = wx.Menu()
        for title, code in CONFIG.PRESENCE_STATUSES:
            status_menu.Append(getattr(ids, code.upper(), wx.ID_ANY), title,
                               kind=wx.ITEM_RADIO)
        status_menu.Check(getattr(ids, self.presence.upper(), wx.ID_ANY), True)

        menu = wx.Menu()
        if self.app.roster.IsShown():
            menu.Append(ids.HIDE, CONFIG.ICON_HIDE_ROSTER)
        else:
            menu.Append(ids.RESTORE, CONFIG.ICON_SHOW_ROSTER)
        menu.AppendSeparator()
        pres = wx.MenuItem(menu, wx.ID_ANY, CONFIG.ICON_PRESENCE_CHANGE,
                           subMenu=status_menu)
        if self.presence in ('online', 'away', 'offline'):
            pres.SetBitmap(wx.Bitmap(img('small_{0}'.format(self.presence))))
        menu.AppendItem(pres)
        prefs = wx.MenuItem(menu, ids.PREFERENCES, CONFIG.ICON_PREFERENCES)
        prefs_img = wx.Image(img('preferences'))
        prefs_img.Rescale(16, 16)
        prefs.SetBitmap(wx.BitmapFromImage(prefs_img))
        menu.AppendItem(prefs)
        menu.AppendSeparator()
        menu.Append(ids.EXIT, CONFIG.ICON_EXIT)
        return menu

    def on_main_action(self, e):
        """Left mouse click on tray icon handling"""
        if self.app.roster.IsShown():
            wx.PostEvent(self.app.roster, ev.HideRoster())
        else:
            wx.PostEvent(self.app.roster, ev.ShowRoster())

    def on_actions_list(self, e):
        """Right mouse click on tray icon handling"""
        self.PopupMenu(self.popup_menu())

    def on_menu_item(self, e):
        """Popup menu item selection handling"""
        if e.Id == ids.RESTORE:
            wx.PostEvent(self.app.roster, ev.ShowRoster())
        elif e.Id == ids.HIDE:
            wx.PostEvent(self.app.roster, ev.HideRoster())
        elif e.Id == ids.EXIT:
            wx.PostEvent(self.app.roster, wx.MenuEvent(
                wx.wxEVT_COMMAND_MENU_SELECTED, wx.ID_EXIT))
        elif e.Id == ids.PREFERENCES:
            wx.PostEvent(self.app.roster, wx.MenuEvent(
                wx.wxEVT_COMMAND_MENU_SELECTED, ids.PREFERENCES))
        elif e.Id == ids.OFFLINE:
            wx.PostEvent(self.app, ev.ChangePresence(status='offline'))
        elif e.Id == ids.AWAY:
            wx.PostEvent(self.app, ev.ChangePresence(status='away'))
        elif e.Id == ids.ONLINE:
            wx.PostEvent(self.app, ev.ChangePresence(status='online'))
