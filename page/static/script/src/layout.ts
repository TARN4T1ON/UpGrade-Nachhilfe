//@TODO: don't use modules for wider support
//@TODO: comment

class state {
    state: boolean = false;

    toggle(
        override: boolean = null
    ) {
        if (this.state == null)
        {
            this.state = false;
        }

        if (override == null)
        {
            this.state = !this.state;
        }
        else
        {
            this.state = override;
        }
    }
}

class stateElement {
    _state: state;

    element: HTMLElement;

    constructor(
        element: HTMLElement
    ) {
        this._state = new state();

        this.element = element;
    }

    handler(event: Event) { }

    toggle(
        override: boolean = null
    ) {
        this._state.toggle(override);
    }
}

class layout {
    elements = {
        "NAV": new stateElement(document.querySelector("nav")),
        "NAV_TOGGLE": new stateElement(document.querySelector("#nav-toggle")),
    };

    listeners = {
        "SCROLL": null,
    };

    constructor() {
        var _nav = this.elements.NAV;
        var _navToggle = this.elements.NAV_TOGGLE;

        _nav.element.style.transform = "translateX(100%)";
        _navToggle.handler = function (event: Event) {
            _navToggle._state.toggle();

            if (_navToggle._state.state)
            {
                _nav.element.style.transform = "translateX(0%)";
            }
            else
            {
                _nav.element.style.transform = "translate(100%)";
            }
        }

        _navToggle.element.addEventListener(
            "click",
            _navToggle.handler
        );

        this.listeners.SCROLL = window.addEventListener(
            "scroll", 
            this.scroll,
            {
                "passive": true
            }
        );
    }

    scroll(event: WheelEvent) {
        var scrollTop = document.documentElement.scrollTop;
        var scrollHeight = document.documentElement.scrollHeight;
        var windowHeight = window.innerHeight;

        document.documentElement.style.setProperty(
            "--scroll-percentage",
            ((scrollTop / (scrollHeight - windowHeight)) * 100).toString() + "%"
        );
        document.documentElement.dataset["scroll"] = scrollTop.toString();
    }
}

export { state, stateElement, layout };