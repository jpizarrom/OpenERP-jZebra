/*---------------------------------------------------------
 * OpenERP base_hello (Example module)
 *---------------------------------------------------------*/

openerp.jzebra = function(openerp) {
    var _t = openerp.web._t,
       _lt = openerp.web._lt;
    openerp.jzebra = {};
    openerp.web.form.widgets.add('jzebra', 'openerp.jzebra.jZebraWidget');

openerp.jzebra.jZebraWidget = openerp.web.form.Field.extend({
    template: 'jzebra-applet',
    start: function() {
        this._super.apply(this, arguments);

        var context = new openerp.web.CompoundContext(this.view.dataset.get_context());
        if (context['__contexts'] && context['__contexts'][0]){
            this.prod = context['__contexts'][0]

            var $input = this.$element.find('input.[value="Load EPL"]');
            $input.click(this.on_load_epl);

            this.jzebra_action_id = this.prod['jzebra_action_id']
        }
    },
    on_load_epl: function() {
            var $input = this.$element.find('#epl');
            var self = this;
            var additional_context = _.extend({
                active_id: this.prod['active_id'],
                active_ids: this.prod['active_ids'],
                active_model: self.widget_parent.dataset.model
            }, this.view.dataset.get_context());
            self.rpc("/web/action/load", {
                action_id: this.jzebra_action_id,
                context: additional_context
            }, function(result) {
                result.result.context = _.extend(result.result.context || {},
                    additional_context);
                result.result.flags = result.result.flags || {};
                result.result.flags.new_window = true;
                action = result.result;
                self.rpc("/web/session/eval_domain_and_context", {
                            contexts: [action.context],
                            domains: []
                        }).then(function(res) {
                            action = _.clone(action);
                            action.context = res.context;
                            var timer, token = new Date().getTime();
                            data = {action: JSON.stringify(action)}
                            data = _.extend({}, data || {},
                                       {session_id: self.session.session_id, token: token});
                            $.ajax({
                                url: '/web/report',
                                data: data,
                                success: function(data){
                                    $input.val(data);
                                },
                                type: 'POST',
                            });
                        });
            });
        },
});

};

// vim:et fdc=0 fdl=0:
