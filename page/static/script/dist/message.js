import { state } from "./helper.js";
import { cookieGet, cookieRemove } from "./cookie.js";
var types;
(function (types) {
    types["SUCCESS"] = "SUCCESS";
    types["WARNING"] = "WARNING";
    types["ERROR"] = "ERROR";
})(types || (types = {}));
class message {
    constructor() {
        this.elements = {
            "message": document.querySelector("#message"),
            "text": document.querySelector("#message .message-text"),
        };
        this.states = {};
        this.handlers = {};
        this.type = null;
        this.message = null;
        this.handleTimeout = null;
        this.timeTimeout = 7500;
        var that = this;
        this.states["message"] = new state();
        this.handlers["message"] = {};
        this.handlers["message"]["click"] = function (event) {
            that.states["message"].toggle(false);
            that.hide();
        };
        this.elements.message.addEventListener("click", this.handlers["message"]["click"]);
        this.fromCookie();
        if (this.type != null) {
            this.show();
        }
    }
    fromCookie(key = "message") {
        var value = cookieGet(key);
        if (value == null)
            return;
        else {
            value = decodeURIComponent(value);
            cookieRemove("message");
        }
        this.fromJSON(value);
    }
    fromJSON(json) {
        var dictionary = JSON.parse(json);
        this.type = dictionary["type"];
        this.message = dictionary["message"];
    }
    show() {
        var that = this;
        if (this.handleTimeout != null) {
            clearTimeout(this.handleTimeout);
            this.handleTimeout = null;
        }
        this.handleTimeout = setTimeout(function () {
            that.hide();
        }, this.timeTimeout);
        this.elements.message.style.display = null;
        this.elements.message.dataset["type"] = this.type;
        this.elements.text.innerText = this.message;
    }
    hide() {
        this.elements.message.style.display = "none";
    }
}
export { types as messageTypes, message };
