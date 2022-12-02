# Copyright (c) 2021, codescientist703 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ChatProfile(Document):
    def set_token(self):
        self.token = frappe.generate_hash()

    def before_save(self):
        self.ip_address = frappe.local.request_ip
