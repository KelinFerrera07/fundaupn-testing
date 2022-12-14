odoo.define('openeducat_dashboard_kpi.FormattingFunction', function(require) {
    "use strict";

    var session = require('web.session')

    return {
        number_shorthand_function: function(num, digits) {
            var negative;
            var si = [{
                    value: 1,
                    symbol: ""
                },{
                    value: 1E3,
                    symbol: "k"
                },{
                    value: 1E6,
                    symbol: "M"
                },{
                    value: 1E9,
                    symbol: "G"
                },{
                    value: 1E12,
                    symbol: "T"
                },{
                    value: 1E15,
                    symbol: "P"
                },{
                    value: 1E18,
                    symbol: "E"
                }];
            if (num < 0) {
                num = Math.abs(num)
                negative = true
            }
            var rx = /\.0+$|(\.[0-9]*[1-9])0+$/;
            var i;
            for (i = si.length - 1; i > 0; i--) {
                if (num >= si[i].value) {
                    break;
                }
            }
            if (negative) {
                return "-" + (num / si[i].value).toFixed(digits).replace(rx, "$1") + si[i].symbol;
            } else {
                return (num / si[i].value).toFixed(digits).replace(rx, "$1") + si[i].symbol;
            }
        },

        currency_monetary_function: function(value, currency_id) {
            var currency = session.get_currency(currency_id);
            if (!currency) {
                return value;
            }
            if (currency.position === "after") {
                return value += ' ' + currency.symbol;
            } else {
                return currency.symbol + ' ' + value;
            }
        },
        convert_to_rgba_function: function(val) {

            var rgba = val.split(',')[0].match(/[A-Za-z0-9]{2}/g);
            rgba = rgba.map(function(v) {
                return parseInt(v, 16)
            }).join(",");
            return "rgba(" + rgba + "," + val.split(',')[1] + ")";

        },
    }

});