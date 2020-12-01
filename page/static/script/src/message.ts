import { state } from "./helper.js";
import { cookieGet, cookieSet, cookieRemove } from "./cookie.js"

enum types {
    SUCCESS = "SUCCESS",
    WARNING = "WARNING",
    ERROR = "ERROR",
}

class message {
    elements = {
        "message": <HTMLElement>document.querySelector("#message"),
        "text": <HTMLElement>document.querySelector("#message .message-text"),
    };

    states = {};
    handlers = {};

    type: types = null;
    message: string = null;

    handleTimeout: number = null;
    timeTimeout: number = 7500;

    constructor() {
        var that = this;

        this.states["message"] = new state();

        this.handlers["message"] = {};
        this.handlers["message"]["click"] = function (
            event: MouseEvent
        ) {
            that.states["message"].toggle(false);

            that.hide();
        }

        this.elements.message.addEventListener(
            "click",
            this.handlers["message"]["click"]
        );

        this.fromCookie();

        if (this.type != null)
        {
            this.show();
        }
    }

    fromCookie(
        key: string = "message"
    ) {
        var value = cookieGet(key);

        if (value == null) return;
        else
        {
            value = decodeURIComponent(value);

            cookieRemove(
                "message"
            );
        }

        this.fromJSON(
            value
        );
    }

    fromJSON(
        json: string
    ) {
        var dictionary = JSON.parse(json);

        this.type = dictionary["type"]
        this.message = dictionary["message"]
    }

    show() {
        var that = this;

        if (this.handleTimeout != null)
        {
            clearTimeout(this.handleTimeout);
            this.handleTimeout = null;
        }

        this.handleTimeout = setTimeout(
            function () {
                that.hide();
            },
            this.timeTimeout
        );

        this.elements.message.style.display = null;

        this.elements.message.dataset["type"] = this.type;
        this.elements.text.innerText = this.message;
    }

    hide() {
        this.elements.message.style.display = "none";
    }
}

export { types as messageTypes, message };