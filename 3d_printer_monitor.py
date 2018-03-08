
# -*- coding: utf8 -*-

import remi.gui as gui
from remi.gui import *
from remi import start, App


class app_3d_printer_monitor(App):
    def __init__(self, *args, **kwargs):
        if not 'editing_mode' in kwargs.keys():
            super(app_3d_printer_monitor, self).__init__(*args, static_file_path='./res/')

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return app_3d_printer_monitor.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        main_container = VBox()
        main_container.attributes['editor_newclass'] = "False"
        main_container.attributes['editor_baseclass'] = "VBox"
        main_container.attributes['editor_constructor'] = "()"
        main_container.attributes['class'] = "VBox"
        main_container.attributes['editor_tag_type'] = "widget"
        main_container.attributes['editor_varname'] = "main_container"
        main_container.style['align-items'] = "center"
        main_container.style['top'] = "1px"
        main_container.style['flex-direction'] = "column"
        main_container.style['height'] = "579px"
        main_container.style['width'] = "525px"
        main_container.style['justify-content'] = "space-around"
        main_container.style['position'] = "absolute"
        main_container.style['overflow'] = "auto"
        main_container.style['margin'] = "0px"
        main_container.style['display'] = "flex"
        main_container.style['background-color'] = "#f7f7f7"
        main_container.style['left'] = "1px"
        sub_container_printjob_status = HBox()
        sub_container_printjob_status.attributes['editor_newclass'] = "False"
        sub_container_printjob_status.attributes['editor_baseclass'] = "HBox"
        sub_container_printjob_status.attributes['editor_constructor'] = "()"
        sub_container_printjob_status.attributes['class'] = "HBox"
        sub_container_printjob_status.attributes['editor_tag_type'] = "widget"
        sub_container_printjob_status.attributes['editor_varname'] = "sub_container_printjob_status"
        sub_container_printjob_status.style['align-items'] = "center"
        sub_container_printjob_status.style['top'] = "1px"
        sub_container_printjob_status.style['flex-direction'] = "row"
        sub_container_printjob_status.style['height'] = "50px"
        sub_container_printjob_status.style['-webkit-order'] = "78331536"
        sub_container_printjob_status.style['width'] = "300px"
        sub_container_printjob_status.style['justify-content'] = "space-between"
        sub_container_printjob_status.style['position'] = "static"
        sub_container_printjob_status.style['overflow'] = "auto"
        sub_container_printjob_status.style['order'] = "4"
        sub_container_printjob_status.style['margin'] = "0px"
        sub_container_printjob_status.style['display'] = "flex"
        sub_container_printjob_status.style['left'] = "1px"
        lbl_printjob_status_value = Label('IDLE')
        lbl_printjob_status_value.attributes['editor_newclass'] = "False"
        lbl_printjob_status_value.attributes['editor_baseclass'] = "Label"
        lbl_printjob_status_value.attributes['editor_constructor'] = "('IDLE')"
        lbl_printjob_status_value.attributes['class'] = "Label"
        lbl_printjob_status_value.attributes['editor_tag_type'] = "widget"
        lbl_printjob_status_value.attributes['editor_varname'] = "lbl_printjob_status_value"
        lbl_printjob_status_value.style['font-size'] = "30px"
        lbl_printjob_status_value.style['-webkit-order'] = "114212016"
        lbl_printjob_status_value.style['top'] = "1px"
        lbl_printjob_status_value.style['height'] = "30px"
        lbl_printjob_status_value.style['width'] = "100px"
        lbl_printjob_status_value.style['position'] = "static"
        lbl_printjob_status_value.style['overflow'] = "auto"
        lbl_printjob_status_value.style['order'] = "1"
        lbl_printjob_status_value.style['margin'] = "0px"
        lbl_printjob_status_value.style['display'] = "block"
        lbl_printjob_status_value.style['left'] = "1px"
        sub_container_printjob_status.append(lbl_printjob_status_value,'lbl_printjob_status_value')
        lbl_printjob_status = Label('Print job status')
        lbl_printjob_status.attributes['editor_newclass'] = "False"
        lbl_printjob_status.attributes['editor_baseclass'] = "Label"
        lbl_printjob_status.attributes['editor_constructor'] = "('Print job status')"
        lbl_printjob_status.attributes['class'] = "Label"
        lbl_printjob_status.attributes['editor_tag_type'] = "widget"
        lbl_printjob_status.attributes['editor_varname'] = "lbl_printjob_status"
        lbl_printjob_status.style['top'] = "1px"
        lbl_printjob_status.style['height'] = "30px"
        lbl_printjob_status.style['-webkit-order'] = "76152816"
        lbl_printjob_status.style['position'] = "static"
        lbl_printjob_status.style['overflow'] = "auto"
        lbl_printjob_status.style['order'] = "0"
        lbl_printjob_status.style['margin'] = "0px"
        lbl_printjob_status.style['display'] = "block"
        lbl_printjob_status.style['left'] = "1px"
        sub_container_printjob_status.append(lbl_printjob_status,'lbl_printjob_status')
        main_container.append(sub_container_printjob_status,'sub_container_printjob_status')
        lbl_title = Label('3D Printer Monitor')
        lbl_title.attributes['editor_newclass'] = "False"
        lbl_title.attributes['editor_baseclass'] = "Label"
        lbl_title.attributes['editor_constructor'] = "('3D Printer Monitor')"
        lbl_title.attributes['class'] = "Label"
        lbl_title.attributes['editor_tag_type'] = "widget"
        lbl_title.attributes['editor_varname'] = "lbl_title"
        lbl_title.style['font-size'] = "30px"
        lbl_title.style['display'] = "block"
        lbl_title.style['top'] = "1px"
        lbl_title.style['height'] = "30px"
        lbl_title.style['-webkit-order'] = "59521456"
        lbl_title.style['position'] = "static"
        lbl_title.style['overflow'] = "auto"
        lbl_title.style['margin'] = "0px"
        lbl_title.style['order'] = "0"
        lbl_title.style['left'] = "1px"
        main_container.append(lbl_title,'lbl_title')
        sub_container_hotend = HBox()
        sub_container_hotend.attributes['editor_newclass'] = "False"
        sub_container_hotend.attributes['editor_baseclass'] = "HBox"
        sub_container_hotend.attributes['editor_constructor'] = "()"
        sub_container_hotend.attributes['class'] = "HBox"
        sub_container_hotend.attributes['editor_tag_type'] = "widget"
        sub_container_hotend.attributes['editor_varname'] = "sub_container_hotend"
        sub_container_hotend.style['align-items'] = "center"
        sub_container_hotend.style['top'] = "1px"
        sub_container_hotend.style['flex-direction'] = "row"
        sub_container_hotend.style['height'] = "50px"
        sub_container_hotend.style['-webkit-order'] = "17469360"
        sub_container_hotend.style['width'] = "300px"
        sub_container_hotend.style['justify-content'] = "space-between"
        sub_container_hotend.style['position'] = "static"
        sub_container_hotend.style['overflow'] = "auto"
        sub_container_hotend.style['order'] = "1"
        sub_container_hotend.style['margin'] = "0px"
        sub_container_hotend.style['display'] = "flex"
        sub_container_hotend.style['left'] = "1px"
        lbl_hotend = Label('HOTEND Temperature')
        lbl_hotend.attributes['editor_newclass'] = "False"
        lbl_hotend.attributes['editor_baseclass'] = "Label"
        lbl_hotend.attributes['editor_constructor'] = "('HOTEND Temperature')"
        lbl_hotend.attributes['class'] = "Label"
        lbl_hotend.attributes['editor_tag_type'] = "widget"
        lbl_hotend.attributes['editor_varname'] = "lbl_hotend"
        lbl_hotend.style['display'] = "block"
        lbl_hotend.style['top'] = "1px"
        lbl_hotend.style['height'] = "30px"
        lbl_hotend.style['-webkit-order'] = "17976304"
        lbl_hotend.style['position'] = "static"
        lbl_hotend.style['overflow'] = "auto"
        lbl_hotend.style['margin'] = "0px"
        lbl_hotend.style['order'] = "0"
        lbl_hotend.style['left'] = "1px"
        sub_container_hotend.append(lbl_hotend,'lbl_hotend')
        lbl_hotend_value = Label('0�')
        lbl_hotend_value.attributes['editor_newclass'] = "False"
        lbl_hotend_value.attributes['editor_baseclass'] = "Label"
        lbl_hotend_value.attributes['editor_constructor'] = "('0�')"
        lbl_hotend_value.attributes['class'] = "Label"
        lbl_hotend_value.attributes['editor_tag_type'] = "widget"
        lbl_hotend_value.attributes['editor_varname'] = "lbl_hotend_value"
        lbl_hotend_value.style['font-size'] = "30px"
        lbl_hotend_value.style['-webkit-order'] = "59575408"
        lbl_hotend_value.style['top'] = "1px"
        lbl_hotend_value.style['height'] = "30px"
        lbl_hotend_value.style['width'] = "100px"
        lbl_hotend_value.style['display'] = "block"
        lbl_hotend_value.style['position'] = "static"
        lbl_hotend_value.style['overflow'] = "auto"
        lbl_hotend_value.style['margin'] = "0px"
        lbl_hotend_value.style['order'] = "1"
        lbl_hotend_value.style['left'] = "1px"
        sub_container_hotend.append(lbl_hotend_value,'lbl_hotend_value')
        main_container.append(sub_container_hotend,'sub_container_hotend')
        sub_container_commands = HBox()
        sub_container_commands.attributes['editor_newclass'] = "False"
        sub_container_commands.attributes['editor_baseclass'] = "HBox"
        sub_container_commands.attributes['editor_constructor'] = "()"
        sub_container_commands.attributes['class'] = "HBox"
        sub_container_commands.attributes['editor_tag_type'] = "widget"
        sub_container_commands.attributes['editor_varname'] = "sub_container_commands"
        sub_container_commands.style['align-items'] = "center"
        sub_container_commands.style['top'] = "1px"
        sub_container_commands.style['flex-direction'] = "row"
        sub_container_commands.style['height'] = "50px"
        sub_container_commands.style['-webkit-order'] = "74485488"
        sub_container_commands.style['width'] = "99%"
        sub_container_commands.style['justify-content'] = "space-around"
        sub_container_commands.style['position'] = "static"
        sub_container_commands.style['overflow'] = "auto"
        sub_container_commands.style['order'] = "5"
        sub_container_commands.style['margin'] = "0px"
        sub_container_commands.style['display'] = "flex"
        sub_container_commands.style['left'] = "1px"
        bt_command_send = Button('SEND')
        bt_command_send.attributes['editor_newclass'] = "False"
        bt_command_send.attributes['editor_baseclass'] = "Button"
        bt_command_send.attributes['editor_constructor'] = "('SEND')"
        bt_command_send.attributes['class'] = "Button"
        bt_command_send.attributes['editor_tag_type'] = "widget"
        bt_command_send.attributes['editor_varname'] = "bt_command_send"
        bt_command_send.style['display'] = "block"
        bt_command_send.style['top'] = "1px"
        bt_command_send.style['height'] = "30px"
        bt_command_send.style['-webkit-order'] = "73641168"
        bt_command_send.style['position'] = "static"
        bt_command_send.style['overflow'] = "auto"
        bt_command_send.style['margin'] = "0px"
        bt_command_send.style['order'] = "2"
        bt_command_send.style['left'] = "1px"
        sub_container_commands.append(bt_command_send,'bt_command_send')
        lbl_command = Label('GCODE')
        lbl_command.attributes['editor_newclass'] = "False"
        lbl_command.attributes['editor_baseclass'] = "Label"
        lbl_command.attributes['editor_constructor'] = "('GCODE')"
        lbl_command.attributes['class'] = "Label"
        lbl_command.attributes['editor_tag_type'] = "widget"
        lbl_command.attributes['editor_varname'] = "lbl_command"
        lbl_command.style['top'] = "1px"
        lbl_command.style['display'] = "block"
        lbl_command.style['-webkit-order'] = "74300624"
        lbl_command.style['position'] = "static"
        lbl_command.style['overflow'] = "auto"
        lbl_command.style['margin'] = "0px"
        lbl_command.style['order'] = "0"
        lbl_command.style['left'] = "1px"
        sub_container_commands.append(lbl_command,'lbl_command')
        link_command_help = Link('http://reprap.org/wiki/G-code','help',True)
        link_command_help.attributes['editor_newclass'] = "False"
        link_command_help.attributes['target'] = "_blank"
        link_command_help.attributes['editor_baseclass'] = "Link"
        link_command_help.attributes['editor_constructor'] = "('http://reprap.org/wiki/G-code','help',True)"
        link_command_help.attributes['class'] = "Link"
        link_command_help.attributes['editor_tag_type'] = "widget"
        link_command_help.attributes['href'] = "http://reprap.org/wiki/G-code"
        link_command_help.attributes['editor_varname'] = "link_command_help"
        link_command_help.style['top'] = "1px"
        link_command_help.style['display'] = "block"
        link_command_help.style['-webkit-order'] = "74300752"
        link_command_help.style['position'] = "static"
        link_command_help.style['overflow'] = "auto"
        link_command_help.style['margin'] = "0px"
        link_command_help.style['order'] = "74300752"
        link_command_help.style['left'] = "1px"
        sub_container_commands.append(link_command_help,'link_command_help')
        txt_gcode_input = TextInput(True,'G28')
        txt_gcode_input.attributes['rows'] = "1"
        txt_gcode_input.attributes['editor_baseclass'] = "TextInput"
        txt_gcode_input.attributes['editor_constructor'] = "(True,'G28')"
        txt_gcode_input.attributes['class'] = "TextInput"
        txt_gcode_input.attributes['autocomplete'] = "off"
        txt_gcode_input.attributes['editor_tag_type'] = "widget"
        txt_gcode_input.attributes['editor_newclass'] = "False"
        txt_gcode_input.attributes['editor_varname'] = "txt_gcode_input"
        txt_gcode_input.attributes['placeholder'] = "G28"
        txt_gcode_input.style['font-size'] = "20px"
        txt_gcode_input.style['width'] = "350px"
        txt_gcode_input.style['top'] = "1px"
        txt_gcode_input.style['height'] = "30px"
        txt_gcode_input.style['-webkit-order'] = "107654000"
        txt_gcode_input.style['display'] = "block"
        txt_gcode_input.style['position'] = "static"
        txt_gcode_input.style['overflow'] = "auto"
        txt_gcode_input.style['margin'] = "0px"
        txt_gcode_input.style['order'] = "1"
        txt_gcode_input.style['resize'] = "none"
        txt_gcode_input.style['left'] = "1px"
        sub_container_commands.append(txt_gcode_input,'txt_gcode_input')
        main_container.append(sub_container_commands,'sub_container_commands')
        bt_emergency_stop = Button('STOP')
        bt_emergency_stop.attributes['editor_newclass'] = "False"
        bt_emergency_stop.attributes['editor_baseclass'] = "Button"
        bt_emergency_stop.attributes['editor_constructor'] = "('STOP')"
        bt_emergency_stop.attributes['class'] = "Button"
        bt_emergency_stop.attributes['editor_tag_type'] = "widget"
        bt_emergency_stop.attributes['editor_varname'] = "bt_emergency_stop"
        bt_emergency_stop.style['font-size'] = "30px"
        bt_emergency_stop.style['-webkit-order'] = "78855728"
        bt_emergency_stop.style['top'] = "1px"
        bt_emergency_stop.style['height'] = "120px"
        bt_emergency_stop.style['order'] = "3"
        bt_emergency_stop.style['width'] = "120px"
        bt_emergency_stop.style['position'] = "static"
        bt_emergency_stop.style['overflow'] = "auto"
        bt_emergency_stop.style['font-weight'] = "bolder"
        bt_emergency_stop.style['margin'] = "0px"
        bt_emergency_stop.style['display'] = "block"
        bt_emergency_stop.style['background-color'] = "#ff1111"
        bt_emergency_stop.style['left'] = "1px"
        main_container.append(bt_emergency_stop,'bt_emergency_stop')
        sub_container_hotbed = HBox()
        sub_container_hotbed.attributes['editor_newclass'] = "False"
        sub_container_hotbed.attributes['editor_baseclass'] = "HBox"
        sub_container_hotbed.attributes['editor_constructor'] = "()"
        sub_container_hotbed.attributes['class'] = "HBox"
        sub_container_hotbed.attributes['editor_tag_type'] = "widget"
        sub_container_hotbed.attributes['editor_varname'] = "sub_container_hotbed"
        sub_container_hotbed.style['align-items'] = "center"
        sub_container_hotbed.style['top'] = "1px"
        sub_container_hotbed.style['flex-direction'] = "row"
        sub_container_hotbed.style['height'] = "50px"
        sub_container_hotbed.style['-webkit-order'] = "17356624"
        sub_container_hotbed.style['width'] = "300px"
        sub_container_hotbed.style['justify-content'] = "space-between"
        sub_container_hotbed.style['position'] = "static"
        sub_container_hotbed.style['overflow'] = "auto"
        sub_container_hotbed.style['order'] = "2"
        sub_container_hotbed.style['margin'] = "0px"
        sub_container_hotbed.style['display'] = "flex"
        sub_container_hotbed.style['left'] = "1px"
        lbl_bed_value = Label('0�')
        lbl_bed_value.attributes['editor_newclass'] = "False"
        lbl_bed_value.attributes['editor_baseclass'] = "Label"
        lbl_bed_value.attributes['editor_constructor'] = "('0�')"
        lbl_bed_value.attributes['class'] = "Label"
        lbl_bed_value.attributes['editor_tag_type'] = "widget"
        lbl_bed_value.attributes['editor_varname'] = "lbl_bed_value"
        lbl_bed_value.style['font-size'] = "30px"
        lbl_bed_value.style['-webkit-order'] = "18323216"
        lbl_bed_value.style['top'] = "1px"
        lbl_bed_value.style['height'] = "30px"
        lbl_bed_value.style['width'] = "100px"
        lbl_bed_value.style['display'] = "block"
        lbl_bed_value.style['position'] = "static"
        lbl_bed_value.style['overflow'] = "auto"
        lbl_bed_value.style['margin'] = "0px"
        lbl_bed_value.style['order'] = "1"
        lbl_bed_value.style['left'] = "1px"
        sub_container_hotbed.append(lbl_bed_value,'lbl_bed_value')
        lbl_bed = Label('BED Temperature')
        lbl_bed.attributes['editor_newclass'] = "False"
        lbl_bed.attributes['editor_baseclass'] = "Label"
        lbl_bed.attributes['editor_constructor'] = "('BED Temperature')"
        lbl_bed.attributes['class'] = "Label"
        lbl_bed.attributes['editor_tag_type'] = "widget"
        lbl_bed.attributes['editor_varname'] = "lbl_bed"
        lbl_bed.style['display'] = "block"
        lbl_bed.style['top'] = "1px"
        lbl_bed.style['height'] = "30px"
        lbl_bed.style['-webkit-order'] = "18091280"
        lbl_bed.style['position'] = "static"
        lbl_bed.style['overflow'] = "auto"
        lbl_bed.style['margin'] = "0px"
        lbl_bed.style['order'] = "0"
        lbl_bed.style['left'] = "1px"
        sub_container_hotbed.append(lbl_bed,'lbl_bed')
        main_container.append(sub_container_hotbed,'sub_container_hotbed')
        sub_container_log = VBox()
        sub_container_log.attributes['editor_newclass'] = "False"
        sub_container_log.attributes['editor_baseclass'] = "VBox"
        sub_container_log.attributes['editor_constructor'] = "()"
        sub_container_log.attributes['class'] = "VBox"
        sub_container_log.attributes['editor_tag_type'] = "widget"
        sub_container_log.attributes['editor_varname'] = "sub_container_log"
        sub_container_log.style['align-items'] = "center"
        sub_container_log.style['border-color'] = "#c9c9c9"
        sub_container_log.style['top'] = "1px"
        sub_container_log.style['flex-direction'] = "column"
        sub_container_log.style['border-width'] = "1px"
        sub_container_log.style['order'] = "6"
        sub_container_log.style['-webkit-order'] = "113811728"
        sub_container_log.style['border-style'] = "dotted"
        sub_container_log.style['width'] = "99%"
        sub_container_log.style['justify-content'] = "space-between"
        sub_container_log.style['position'] = "static"
        sub_container_log.style['overflow'] = "auto"
        sub_container_log.style['margin'] = "0px"
        sub_container_log.style['display'] = "flex"
        sub_container_log.style['background-color'] = "#f0f0f0"
        sub_container_log.style['left'] = "1px"
        lbl_log = Label('LOG')
        lbl_log.attributes['editor_newclass'] = "False"
        lbl_log.attributes['editor_baseclass'] = "Label"
        lbl_log.attributes['editor_constructor'] = "('LOG')"
        lbl_log.attributes['class'] = "Label"
        lbl_log.attributes['editor_tag_type'] = "widget"
        lbl_log.attributes['editor_varname'] = "lbl_log"
        lbl_log.style['display'] = "block"
        lbl_log.style['top'] = "1px"
        lbl_log.style['height'] = "30px"
        lbl_log.style['-webkit-order'] = "109084816"
        lbl_log.style['position'] = "static"
        lbl_log.style['overflow'] = "auto"
        lbl_log.style['margin'] = "0px"
        lbl_log.style['order'] = "0"
        lbl_log.style['left'] = "1px"
        sub_container_log.append(lbl_log,'lbl_log')
        list_log = ListView(True)
        list_log.attributes['editor_newclass'] = "False"
        list_log.attributes['editor_baseclass'] = "ListView"
        list_log.attributes['editor_constructor'] = "(True)"
        list_log.attributes['class'] = "ListView"
        list_log.attributes['editor_tag_type'] = "widget"
        list_log.attributes['editor_varname'] = "list_log"
        list_log.style['width'] = "100%"
        list_log.style['top'] = "1px"
        list_log.style['height'] = "150px"
        list_log.style['-webkit-order'] = "71761648"
        list_log.style['display'] = "block"
        list_log.style['position'] = "static"
        list_log.style['overflow'] = "auto"
        list_log.style['margin'] = "0px"
        list_log.style['order'] = "1"
        list_log.style['left'] = "1px"
        sub_container_log.append(list_log,'list_log')
        main_container.append(sub_container_log,'sub_container_log')
        main_container.children['bt_command_send'].set_on_click_listener(self.onclick_bt_command_send)
        main_container.children['bt_emergency_stop'].set_on_click_listener(self.onclick_bt_emergency_stop)
        

        self.main_container = main_container
        return self.main_container
    
    def onclick_bt_command_send(self,emitter):
        pass

    def onclick_bt_emergency_stop(self,emitter):
        pass



#Configuration
configuration = {'config_multiple_instance': True, 'config_address': '0.0.0.0', 'config_start_browser': True, 'config_enable_file_cache': True, 'config_project_name': 'app_3d_printer_monitor', 'config_resourcepath': './res/', 'config_port': 8081}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(app_3d_printer_monitor, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
