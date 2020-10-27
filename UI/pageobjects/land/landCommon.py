# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.land.land_details_entity import LandDetailsEntity
from config.land.land_common_entity import LandCommonEntity
from utils.logger import logger

class LandCommonPage(BasePage):
    def is_details_page(self,title):
        """
        #Details Page
        :param:title
        :return:
        """
        if self.find_element(LandCommonEntity().get_default_text(title)):
            return True
        else:
            return False

    def switch_tab(self,title,tabName):
        """
        #Details Page Switch Tab
        :param:title, tabName
        :return:
        """
        if self.is_details_page(title) == True:
            self.find_element_by_wait("xpath", LandCommonEntity().get_record_tab(tabName))
            self.click(LandCommonEntity().get_record_tab(tabName))

    def not_selected(self,section,row):
        """
        # Not selected record
        :param : section
        :param : row
        :return:
        """
        selected = self.find_element(
            LandCommonEntity().get_select_record(section, row)).get_attribute('style')
        if "background" in  selected:
            pass
        else:
            return True

    def get_tips_msg(self):
        """
        # get the msg
        :return:
        """
        self.sleep(2)
        return  self.find_element(LandCommonEntity.tips_msg).text

    def entity_operator(self,title,sectionName,buttonName,row,textarea):
        """
        #Tabs
        :param sectionName,buttonName,row
        :return:
        """
        if self.is_details_page(title) == True:
            section_list = self.find_elements(LandCommonEntity.section_list)
            # print(section_list)
            section_item = None
            for i, item in enumerate(section_list):
                if sectionName == item.text:
                    section_item = (i + 1, item)
                    break
            if section_item is None:
                logger.info(msg="sectionName %s not found!" % sectionName)
            else:
                # self.scroll_into_view(LandDetailsEntity().get_section_name(sectionName))
                if buttonName in ("New", "Relate"):
                    pass
                elif self.exist_element(LandCommonEntity().get_section_records(section_item[0])):
                    if self.not_selected(section_item[0], row) == True:
                        self.click(LandCommonEntity().get_select_record(section_item[0], row))
                    if buttonName in ("Details", "History"):
                        table = []
                        table_list = self.find_elements(LandCommonEntity().get_column_value(section_item[0], row))
                        for i, item in enumerate(table_list):
                            value = item.text
                            table.append(value)
                        print("#####")
                        print(table)
                        print("#####")
                        self.click(LandCommonEntity().get_section_operator(section_item[0], buttonName))
                        s = []
                        if buttonName == "Details":
                            input_list = self.find_elements(LandCommonEntity.input_value)
                            for a, item in enumerate(input_list):
                                value = item.get_attribute('value')
                                s.append(value)
                            if textarea == 1:
                                for b, item in enumerate(self.find_elements(LandCommonEntity.textarea_value)):
                                    value = item.text
                                    s.append(value)
                        else:
                            history_list = self.find_elements(LandCommonEntity().get_history_value(row))
                            for a, item in enumerate(history_list):
                                value = item.text
                                s.append(value)
                        print("!!!!")
                        print(s)
                        print("!!!!")
                        self.sleep(2)
                        self.execute_script_click(LandCommonEntity.close)
                        if set(table) < set(s) or set(s) < set(table) or table == s:
                            return True
                        else:
                            return False
                self.click(LandCommonEntity().get_section_operator(section_item[0], buttonName))


    def special_operator(self,title,sectionName,buttonName,row):
        """
        #Tabs
        :param sectionName,buttonName,row
        :return:
        """
        if self.is_details_page(title) == True:
            special_section_list = self.find_elements(LandCommonEntity.special_section_list)
            # print(special_section_list)
            section_item = None
            for i, item in enumerate(special_section_list):
                if sectionName == item.text:
                    section_item = (i + 1, item)
                    break
            if section_item is None:
                logger.info(msg="sectionName %s not found!" % sectionName)
            else:
                # self.scroll_into_view(LandDetailsEntity().get_section_name(sectionName))
                if sectionName in ("Location From County Seat", "Location", "Characteristics", "Management", "Uplands",
                                   "Survey"):
                    if buttonName == "History":
                        seciton_value_list = []
                        field_list = self.find_elements(LandCommonEntity().get_section_value(section_item[0]))
                        for a, item in enumerate(field_list):
                            value = item.get_attribute('value')
                            seciton_value_list.append(value)
                        print("#####")
                        print(seciton_value_list)
                        print("#####")
                        self.click(LandCommonEntity().get_specail_operator(section_item[0], buttonName))
                        s = []
                        history_list = self.find_elements(LandCommonEntity().get_history_value(row))
                        for a, item in enumerate(history_list):
                            value = item.text
                            s.append(value)
                        print("!!!!")
                        print(s)
                        print("!!!!")
                        self.sleep(2)
                        self.execute_script_click(LandCommonEntity.close)
                        if set(seciton_value_list) < set(s) or set(s) < set(
                                seciton_value_list) or seciton_value_list == s:
                            return True
                        else:
                            return False
                    self.sleep(2)
                    self.click(LandCommonEntity().get_specail_operator(section_item[0], buttonName))
                    self.sleep(2)

    def delete(self):
        """
        # Execute delete
        :return:
        """
        self.sleep(1)
        self.click(LandCommonEntity.delete_confirm)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

    def required_validation(self):
        self.sleep(1)
        field_name_list = []
        msg_required_list = []
        for i in range(1,len(self.find_elements(LandCommonEntity.field_section))+1):
            for j in range(1,len(self.find_elements(LandCommonEntity().get_fields_of_section(i)))+1):
                if  self.exist_element(LandCommonEntity().get_required_name(i,j)) != False:
                    field_name_list.append((self.find_element(LandCommonEntity().get_fields_name(i,j)).text).rstrip(
                        '*') + " is required.")
        print("!!!!!")
        print(field_name_list)
        print("!!!!!")
        self.sleep(1)
        self.click(LandCommonEntity().get_land_button("Save"))
        required_message_list = self.find_elements(LandCommonEntity.required_field_message)
        for i,item in enumerate(required_message_list):
            value = item.text
            msg_required_list.append(value)
        print("#####")
        print(msg_required_list)
        print("#####")
        # self.sleep(1)
        # if flag == 1:
        #     self.execute_script_click(LandCommonEntity.close)
        # else:
        #     self.execute_script_click(LandCommonEntity().get_land_button("Cancel"))
        if  field_name_list == msg_required_list:
            return True
        else:
            return False


    def top_operate(self,title,buttonName,acitonName):
        """
        # Action Drop List
        :param : buttonName，acitonName
        :return:
        """
        #self.scroll_into_view(CustomerRecordEntity().get_customer_operate(buttonName))
        if self.is_details_page(title) == True:
            self.click(LandCommonEntity().get_top_operate(buttonName))
            if buttonName == "Actions ":
                self.click(LandCommonEntity().get_actions(acitonName))
                if acitonName == "Delete":
                    self.delete()







