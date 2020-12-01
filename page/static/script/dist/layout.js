import { state } from "./helper.js";
class layout {
    constructor() {
        this.elements = {
            "nav": document.querySelector("nav"),
            "navToggle": document.querySelector("#nav-toggle"),
        };
        this.states = {};
        this.handlers = {};
        var that = this;
        this.states["navToggle"] = new state();
        this.handlers["navToggle"] = {};
        this.handlers["navToggle"]["click"] = function (event) {
            that.states["navToggle"].toggle();
            if (that.states["navToggle"].state)
                that.elements.nav.style.transform = "translateX(0%)";
            else
                that.elements.nav.style.transform = "translate(100%)";
        };
        this.elements.navToggle.addEventListener("click", this.handlers["navToggle"]["click"]);
        this.handlers["window"] = {};
        this.handlers["window"]["scroll"] = function (event) {
            var scrollTop = document.documentElement.scrollTop;
            var scrollHeight = document.documentElement.scrollHeight;
            var windowHeight = window.innerHeight;
            document.documentElement.style.setProperty("--scroll-percentage", ((scrollTop / (scrollHeight - windowHeight)) * 100).toString() + "%");
            document.documentElement.dataset["scroll"] = scrollTop.toString();
        };
        window.addEventListener("scroll", this.handlers["window"]["scroll"], {
            "passive": true
        });
        this.elements.nav.style.transform = "translateX(100%)";
    }
}
export { layout };
