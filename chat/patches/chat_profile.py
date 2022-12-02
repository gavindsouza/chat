import frappe
from contextlib import contextmanager


@contextmanager
def autocommit():
    flag_value = frappe.db.auto_commit_on_many_writes
    frappe.db.auto_commit_on_many_writes = True
    yield
    frappe.db.auto_commit_on_many_writes = flag_value


def execute():
    with autocommit():
        for chat_profile in frappe.get_all("Chat Profile", fields=["name", "token"]):
            frappe.rename_doc(
                "Chat Profile",
                chat_profile.name,
                chat_profile.token,
                force=True,
                show_alert=False,
            )
