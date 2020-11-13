class state {
    constructor() {
        this.state = false;
    }
    toggle(override = null) {
        if (this.state == null) {
            this.state = false;
        }
        if (override == null) {
            this.state = !this.state;
        }
        else {
            this.state = override;
        }
    }
}
class stateElement {
    constructor(element) {
        this._state = new state();
        this.element = element;
    }
    handler(event) { }
    toggle(override = null) {
        this._state.toggle(override);
    }
}
class layout {
    constructor() {
        this.elements = {
            "NAV": new stateElement(document.querySelector("nav")),
            "NAV_TOGGLE": new stateElement(document.querySelector("nav-toggle")),
        };
        var _nav = this.elements.NAV;
        var _navToggle = this.elements.NAV_TOGGLE;
        _nav.element.style.transform = "translateX(100%)";
        _navToggle.handler = function (event) {
            _navToggle._state.toggle();
            if (_navToggle._state.state) {
                _nav.element.style.transform = "translateX(0%)";
            }
            else {
                _nav.element.style.transform = "translate(100%)";
            }
        };
        _navToggle.element.addEventListener("click", _navToggle.handler);
    }
}
export { state, stateElement, layout };
