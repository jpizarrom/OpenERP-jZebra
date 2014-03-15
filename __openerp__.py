# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (c) 2010 Juan Pizarro <jpizarrom@gmail.com> All Rights Reserved.
#
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "jZebra",
    "category": "Hidden",
    "description":
        """
        OpenERP Web example module.
        """,
    "version": "2.0",
    "depends": ['product','web','report_aeroo_epl2'],
    "update_xml": [
        #~ "jzebra.xml",
        "wizard/printer_view.xml",
    ],
    #~ 'css': [
        #~ 'static/css/jzebra.css',
    #~ ],
    'js': [
#        'static/lib/backbone/backbone-0.5.3.js',
        'static/js/jzebra.js',
        #~ 'static/lib/jsquery.js',
        #~ 'static/lib/jzebra.js',
#        'jzebrasrc/js/PluginDetect.js',
    ],
    'qweb': [
        'static/xml/jzebra.xml',
    ],
    'active': False,
    #~ 'web_preload': False,
}
