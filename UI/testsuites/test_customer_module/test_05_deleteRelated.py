#-*- coding: UTF-8 -*-
import unittest
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from pageobjects.customer.customerRecord import CustomerRecordPage
from pageobjects.common.topMenu import TopMenuPage
from utils.base_page import BasePage

class deleteRelated(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).is_homepage()
        HomePage(cls.driver).quick_entrance("Customers","C000048473",2)
        BasePage(cls.driver).switch_to_handle(1)

    def test_01_customer_delete(self):
        u"""delete customer"""
        CustomerRecordPage(self.driver).top_operate("Actions ", "Delete")
        self.assertTrue(CustomerRecordPage(self.driver).delete_related("Customer"))

    def test_02_Address_delete(self):
        u"""delete address"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete_related("Address"))

    def test_03_contacts_delete(self):
        u"""delete contacts"""
        CustomerRecordPage(self.driver).switch_tab("Contacts")
        CustomerRecordPage(self.driver).contact_operator("Contacts", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete_related("Contact"))

    def test_04_email_delete(self):
        u"""delete contact email"""
        CustomerRecordPage(self.driver).contact_operator("Email", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete_related("Email"))

    def test_05_phone_delete(self):
        u"""delete contact phone"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete_related("Phone"))


