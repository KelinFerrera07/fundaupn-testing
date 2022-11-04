odoo.define('openeducat_gms.batch_on_courses_gms', function (require) {
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

    var  BatchRegister = Widget.extend({
        events:{
            'change #course_dropdown': '_onChangeCourse',
            'change #academic_year_dropdown': '_onChangeAcademicYear',
            'change select[name="grievance_category_id"]': '_onChangeCategory',
            'click .gms-submit-grievance': '_onClickSubmit',
        },
        xmlDependencies: ['/openeducat_grievance_enterprise/static/src/xml/custom.xml'],

        init: function(){
            this._super.apply(this,arguments);
        },
        start: function () {
            var self = this;
            $(".appeal_grievance_category").prop("disabled", true);
            return this._super().then(function(){
                self._onChangeCourse();
                self._onChangeAcademicYear();
                self._onChangeCategory();
            });
        },

         _onClickSubmit: function(e){
            e.preventDefault();

            var $input = $('<input/>',{
                name: 'is_state_change',
                type: 'hidden',
                value: true,
            });
            $('form').append($input);
            $('form').submit();
         },

        _onChangeCourse: function(){
            var course_id = $('#course_dropdown').val();
            ajax.jsonRpc('/get/grievance/course_data', 'call',{
                'course_id': course_id,
            }).then(function (data) {
                if (data) {
                    var batch_data = qweb.render('GetBatchData',{
                        batches: data['batch_list'],
                        selected_id: $('#batch_on_courses_gms').data('selected') || false,
                });
                $('#batch_on_courses_gms').html(batch_data);
              }
            });
        },

        _onChangeAcademicYear: function(){
            var academic_year_id = $('#academic_year_dropdown').val();
            ajax.jsonRpc('/get/academic_term_data', 'call',
                {
                'academic_year_id': academic_year_id,
                }).then(function (data) {
                    if (data) {
                        var academic_term_data = qweb.render('GetTermData',{
                            terms: data['academic_term_list'],
                            selected_id: $('#term_on_academic_year').data('selected') || false,
                        });
                        $('#term_on_academic_year').html(academic_term_data);
                  }
            });
        },

        _onChangeCategory: function(){
            var self = this;
            var $selected = $('select[name="grievance_category_id"]').find('option:selected');
            if($selected.data('academic') == 'academic') {
                $('.non_academic_year').show();
                $('.non_academic_year').each( function(){
                    self._toggleRequired($(this).find('select, input'), true);
                });
            } else {
                $('.non_academic_year').hide();
                $('.non_academic_year').each( function(){
                    self._toggleRequired($(this).find('select, input'), false);
                });
            }
        },

        _toggleRequired: function($element, state){
            $element.each( function(){
                $(this).attr('required', state);
            });
        },
    });
    websiteRootData.websiteRootRegistry.add(BatchRegister, '.grievance_portal_form');
});