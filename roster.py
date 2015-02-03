# -*- coding: utf-8 -*-
"""
.. module:: roster
   :platform: Unix, Windows
   :synopsis: Roster window behavior (only a part of the module)

.. moduleauthor:: Anton Konyshev <anton.konyshev@gmail.com>

"""

import wx

from gui_roster import RosterGUI
from dialogs import AuthDialog, PreferencesDialog, SystemStateDialog
from dialogs import SummaryStatisticsDialog, BanReasonDialog
from config import CONFIG
from utils import gt as _
import events as ev
import ids


class Roster(RosterGUI):
    """Roster window behavior definition"""

    def event_table(self):
        """Roster event table"""
        self.Bind(ev.HIDE_ROSTER_EVENT, self.on_hide)  # ev.HideRoster
        self.Bind(wx.EVT_CLOSE, self.on_hide)  # wx.CloseEvent

    def on_hide(self, e):
        """Hide event handling"""
        if self.app.load_config('iconize_on_close', True):
            self.Hide()
        else:
            wx.PostEvent(
                self, wx.MenuEvent(wx.wxEVT_COMMAND_MENU_SELECTED, wx.ID_EXIT))

    def on_show(self, e):
        """Show event handling"""
        self.Show()
