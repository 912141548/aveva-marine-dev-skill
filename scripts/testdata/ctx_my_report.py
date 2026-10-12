# -*- coding: utf-8 -*-
"""ctx_my_report.py -- Vitesse context menu: show hull panel report.
Deploy to: Vitesse\\Context_Menu\\ctx_my_report.py
"""
import kcs_draft
import kcs_ui
from my_report_helpers import get_real, get_string

def run(*args):
    if not hasattr(kcs_draft, 'ContextElement') or kcs_draft.ContextElement is None:
        kcs_ui.message_confirm('No element under cursor!')
        return
    model = getattr(kcs_draft, 'ContextModel', None)
    if model is None:
        kcs_ui.message_confirm('Not a model element.')
        return
    panel = model.get_name()
    lines = ['PANEL  %s' % panel]
    thi = get_real("HULL.PANEL('%s').PLA(1).THICKNESS" % panel)
    if thi is not None:
        lines.append('PLATE   t=%s mm' % thi)
    qual = get_string("HULL.PANEL('%s').PLA(1).QUALITY.STRING" % panel)
    if qual:
        lines.append('QUALITY %s' % qual)
    kcs_ui.message_confirm('\n'.join(lines))
