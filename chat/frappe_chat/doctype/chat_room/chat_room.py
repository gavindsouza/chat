# Copyright (c) 2021, codescientist703 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ChatRoom(Document):
	def get_members(self):
		member_list = []

		if self.members:
			member_list.extend(x.strip() for x in self.members.split(","))

		if self.guest:
			member_list.append(frappe.db.get_value("Chat Profile", self.guest, "email"))

		if self.users:
			member_list.extend(x.user for x in self.users)

		if "Guest" in member_list:
			member_list.remove("Guest")

		return member_list