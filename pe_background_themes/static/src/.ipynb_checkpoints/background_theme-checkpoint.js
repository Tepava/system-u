/** @odoo-module */
odoo.define('pe_background_themes.BackgroundTheme', function (require) {
    
import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from 'web.utils';
var rpc = require('web.rpc');

rpc.query({model: 'res.config.settings',method: 'get_value_from_company',args: [0],}).then(function(values){
    self.colors = values;
    console.log("values",values);
                
        if (values.nav_bg_color !== false){
            document.documentElement.style.setProperty("--navbar-color",values.nav_bg_color);
        }
        if (values.nav_ft_color !== false){
            document.documentElement.style.setProperty("--navbar-txt-color",values.nav_ft_color);
        }
                
        if (values.btn_hover_color !== false){
            document.documentElement.style.setProperty("--btn-hover-color",values.btn_hover_color);
        }
                
        if (values.bg_color !== false){
            document.documentElement.style.setProperty("--background-color",values.bg_color);
        }
                
        if (values.bg_image !== false){
            document.documentElement.style.setProperty("--background-image",'url(data:image/png;base64,'+values.bg_image+')');
        }
    });
});