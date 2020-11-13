import { layout } from "./layout.js";
var _layout;
function main() {
    _layout = new layout();
    window._layout = _layout;
}
window.addEventListener("load", main);
