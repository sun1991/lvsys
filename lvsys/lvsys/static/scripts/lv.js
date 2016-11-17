function get_vm(index, the_date, config){
    var vm = new Vue({
        el: '#m' + the_date.month + 'd' + the_date.day,
        data: {
            id: index + 1,
            cf: config,
            mm: the_date.month,
            dd: the_date.day,
            lv: the_date.lv_type,
            hld: the_date.is_holiday,
            apr: the_date.is_approved
        },
        computed:{
            to_string: function(){
                return 'id:' + this.id
                    + ' mm:' + this.mm + ' dd:' + this.dd
                    + ' lv:' + this.lv + ' apr:' + this.apr
                    + ' hld:' + this.hld;
            },
            to_color: function () {
                if (this.hld) {
                    return '#777'; // holiday
                } else {
                    return this.cf.lv_to_color(this.lv);
                }
            },
            style_lv: function () {
                var background = null;
                if (this.hld) {
                    background = '#777'; // holiday
                } else {
                    background = this.cf.lv_to_color(this.lv);
                }

                var cur = this.is_disabled ? "no-drop" : "default";

                return {
                    background: background,
                    cursor: cur
                };
            },
            is_disabled: function(){
                if (this.hld === 1 || this.apr === 1) {
                    return true;
                } else {
                    return false;
                }
            },
            is_approved: function(){
                return this.apr === 1 ? true : false;
            },
            check_state:{
                get: function () {
                    if (this.hld) {
                        return true;
                    } else {
                        return this.lv > 0 ? true : false;
                    }
                },
                set: function (newValue) {
                    // holiday will always has lv = 0
                    if (newValue) {
                        this.lv = this.cf.lv;
                        this.cf.re_dict[this.id] = this.cf.lv;
                    } else {
                        this.lv = 0;
                        this.cf.re_dict[this.id] = null;
                    }

                    this.cf.lv_changed_callback();
                }
            }
        },
        methods:{
            user_click: function(event){
                console.log('user_click: ' + this.to_string);
            }
        }
    });

    return vm;
}

function prepare_binding(lvdate_list, lvtype_list){

    var vm_dict = {};
    var vm_list = [];
    var config = {
        lv: 1,
        re_dict: {},
        lv_to_color: function (lv_type) {
            switch (lv_type) {
                case 1:
                    return '#6F6';
                case 2:
                    return '#F55';
                default:
                    return '#FFF';
            }
        },
        lv_changed_callback: function(){}
        //_lv_changed: function () {
        //    this.lv_changed_callback();
        //}
    };

    for(var index=0; index<lvdate_list.length; index++){
        var the_date = lvdate_list[index];
        var vm = get_vm(index, the_date, config);

        var key = 'm' + the_date.wk + 'd' + the_date.dd;
        vm_dict[key] = vm;
        vm_list.push(vm);
    }

    var vm_lvtype = new Vue({
        el: '#lvtype_board',
        data: {
            cf: config
        }
    });

    return {
        vm_list: vm_list,
        vm_dict: vm_dict,
        vm_lvtype: vm_lvtype,
        config: config
    };
}


