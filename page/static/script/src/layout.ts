import { state } from "./helper.js";

class layout {
    elements = {
        "nav": document.querySelector("nav"),
        "navToggle": document.querySelector("#nav-toggle"),
    };

    states = {};
    handlers = {};

    constructor() {
        var that = this;

        //navToggle

        this.states["navToggle"] = new state();

        this.handlers["navToggle"] = {};
        this.handlers["navToggle"]["click"] = function (
            event: MouseEvent
        ): void {
            that.states["navToggle"].toggle();

            if (that.states["navToggle"].state) that.elements.nav.style.transform = "translateX(0%)";
            else that.elements.nav.style.transform = "translate(100%)";
        }

        this.elements.navToggle.addEventListener(
            "click",
            this.handlers["navToggle"]["click"]
        );

        //scroll

        this.handlers["window"] = {};
        this.handlers["window"]["scroll"] = function (
            event: WheelEvent
        ): void {
            var scrollTop = document.documentElement.scrollTop;
            var scrollHeight = document.documentElement.scrollHeight;
            var windowHeight = window.innerHeight;

            document.documentElement.style.setProperty(
                "--scroll-percentage",
                ((scrollTop / (scrollHeight - windowHeight)) * 100).toString() + "%"
            );
            document.documentElement.dataset["scroll"] = scrollTop.toString();
        }

        window.addEventListener(
            "scroll",
            this.handlers["window"]["scroll"],
            {
                "passive": true
            }
        );

        //nav

        this.elements.nav.style.transform = "translateX(100%)";
    }
}

export { layout };