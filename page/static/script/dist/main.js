import { layout } from "./layout.js";
import { cookieGet, cookieSet, cookieRemove } from "./cookie.js";
import { message } from "./message.js";
var _layout;
var _message;
function main() {
    _layout = new layout();
    window._layout = _layout;
    window.cookieGet = cookieGet;
    window.cookieSet = cookieSet;
    window.cookieRemove = cookieRemove;
    _message = new message();
    window._message = _message;
}
window.addEventListener("load", main);
