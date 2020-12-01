//@TODO: comment

import { state } from "./helper.js";
import { layout } from "./layout.js";
import { cookieGet, cookieSet, cookieRemove } from "./cookie.js";
import { messageTypes, message } from "./message.js";

var _layout: layout;
var _message: message;

function main() {
    _layout = new layout();

    (<any>window)._layout = _layout;

    (<any>window).cookieGet = cookieGet;
    (<any>window).cookieSet = cookieSet;
    (<any>window).cookieRemove = cookieRemove;

    _message = new message();

    (<any>window)._message = _message;
}

window.addEventListener(
    "load",
    main
);