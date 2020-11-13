import { state, stateElement, layout } from "./layout.js";

var _layout;

function main() {
    _layout = new layout();

    (<any>window)._layout = _layout;
}

window.addEventListener(
    "load",
    main
);