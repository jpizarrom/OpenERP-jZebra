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

import time
from tools.translate import _

from osv import osv, fields

class jzebra_printer(osv.osv_memory):
    _name = "jzebra.printer"
    _description = 'Make Delievery'

    _columns = {
        'product_id': fields.boolean('product product', required=True),
    }

#    def default_get(self, cr, uid, fields, context=None):
#        res = super(jzebra_printer, self).default_get(cr, uid, fields, context=context)
#        order_obj = self.pool.get('product.product')
#        for order in order_obj.browse(cr, uid, context.get('active_ids', []), context=context):
#             res.update({'product_id': order.id})
             
#        return res

jzebra_printer()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

