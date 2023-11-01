from django.http import HttpRequest
from wagtail import hooks
from .dash_panels import ShortcutsPanel


@hooks.register('construct_reports_menu', order=1)
def hide_reports_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'workflows']
    menu_items[:] = [item for item in menu_items if item.name != 'workflow-tasks']
    menu_items[:] = [item for item in menu_items if item.name != 'aging-pages']
    menu_items[:] = [item for item in menu_items if item.name != 'locked-pages']


@hooks.register('construct_main_menu', order=2)
def hide_snippets_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'documents']
    menu_items[:] = [item for item in menu_items if item.name != 'explorer']
    menu_items[:] = [item for item in menu_items if item.name != 'images']
    menu_items[:] = [item for item in menu_items if item.name != 'help']


@hooks.register("construct_settings_menu", order=3)
def hide_user_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "workflows"]
    menu_items[:] = [item for item in menu_items if item.name != "workflow-tasks"]
    menu_items[:] = [item for item in menu_items if item.name != "redirects"]
    menu_items[:] = [item for item in menu_items if item.name != "sites"]
    menu_items[:] = [item for item in menu_items if item.name != "collections"]


@hooks.register('construct_homepage_panels', order=4)
def add_another_welcome_panel(request, panels):
    panels[:] = [panel for panel in panels if panel.name != "site_summary"]
    panels[:] = [panel for panel in panels if panel.name != "workflow_pages_to_moderate"]
    panels[:] = [panel for panel in panels if panel.name != "pages_for_moderation"]
    panels[:] = [panel for panel in panels if panel.name != "user_pages_in_workflow_moderation"]
    panels[:] = [panel for panel in panels if panel.name != "locked_pages"]

    panels.append(ShortcutsPanel())

