odoo.define('openeducat_parent_enterprise.portal_view', function (require) {
    "use strict";
    var core = require('web.core');
    var Dialog = require("web.Dialog");
    var session = require('web.session');
    var ajax = require('web.ajax');
    var Widget = require('web.Widget');
    var websiteRootData = require('website.root');
    var utils = require('web.utils');
    var _t = core._t;
    var qweb = core.qweb;
    var wUtils = require('website.utils');

    var PortalViewWidget = Widget.extend({
        init: function(){
            $('.list-group-item').addClass('parent_dashboard_element_main_body');
            this._super.apply(this,arguments);
        },
        start: function () {
            return this._super();
        },
    });
    websiteRootData.websiteRootRegistry.add(PortalViewWidget, '.parent_tile_portal');
});
