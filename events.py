# -*- coding: utf-8 -*-
"""
.. module:: events
   :platform: Unix, Windows
   :synopsis: Opertor application events definition (only a part of the module)

.. moduleauthor:: Anton Konyshev <anton.konyshev@gmail.com>

"""

import wx.lib.newevent


ShowRoster, SHOW_ROSTER_EVENT = wx.lib.newevent.NewEvent()
"""Command to show roster window.

Receivers:
    Roster (wx.Frame): roster window.
"""

HideRoster, HIDE_ROSTER_EVENT = wx.lib.newevent.NewEvent()
"""Command to hide roster window.

Receivers:
    Roster (wx.Frame): roster window.
"""

ChangePresence, CHANGE_PRESENCE_EVENT = wx.lib.newevent.NewEvent()
"""Command to change current presence status.

Receivers:
    Oper (wx.App): application object.

Kwargs:
    status (str): new status (may be 'online', 'offline', 'away').
    prompt (str): a message for displaying in the authentication dialog
                  (Default is None).
"""

SignOut, SIGN_OUT_EVENT = wx.lib.newevent.NewEvent()
"""Command to disconnect from a server and set the 'offline' presence.

Receivers:
    Oper (wx.App): an application object.

Kwargs:
    response (bool): whether to post the PresenceUpdated event after
                     disconnection (default is True).
"""

SignIn, SIGN_IN_EVENT = wx.lib.newevent.NewEvent()
"""Command to create a transport instance and connect to a server.

Receivers:
    Oper (wx.App): an application object.

Kwargs:
    login (str): operator's username.
    password (str): operator's password.
"""

ConfigUpdate, CONFIG_UPDATE_EVENT = wx.lib.newevent.NewEvent()
"""Notification about the changing of user's configuration.

Receivers:
    Oper (wx.App): an application object (saves config).
    Roster (wx.Frame): applies config in the roster window.
    Chat (wx.Frame): applies config in the chat window.
    Notify (wx.lib.agw.ToasterBox): applies config notification params.

Kwargs:
    params (dict): changed parameters.
    full (bool): (for Roster) apply all available parameters, not only which
                 contains in params dict (Default is False).
"""

RecvRequisition, RECV_REQUISITION_EVENT = wx.lib.newevent.NewEvent()
"""Notification about the receiving of a new request.

Receivers:
    Oper (wx.App): appends history for the application stories dict.
    Roster (wx.Frame): appends task for the tasks list.
    Icon (wx.TaskBarIcon): show balloon about new task.
    Chat (wx.Frame): show actual conversation history.

Kwargs:
    history (datatypes.History): task content.
"""

FailedAuth, FAILED_AUTH_EVENT = wx.lib.newevent.NewEvent()
"""Notification about failed authentication.

Receivers:
    Roster (wx.Frame): the roster window.
"""

ChatRequested, CHAT_REQUESTED_EVENT = wx.lib.newevent.NewEvent()
"""Command to open the chat window for conversation.

Receivers:
    Oper (wx.App): Create and show the chat window.

Kwargs:
    history (datatypes.History): Selected history.
"""

SendMessage, SEND_MESSAGE_EVENT = wx.lib.newevent.NewEvent()
"""Command to send a message to an interlocutor.

Receivers:
    Oper (wx.App): Command to the transport component for the message sending.

Kwargs:
    message (str): Message content.
    history (datatypes.History): Conversation instance.
"""
