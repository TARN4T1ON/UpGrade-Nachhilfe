const _path = "/";
const _domain = location.hostname;

function cookieRemove(
    key: string,
    path: string = _path,
    domain: string = _domain
) {
    var _path: string = "";
    if (path != null) _path = `path=${path};`;

    var _domain: string = "";
    if (domain != null) _domain = `domain=${domain};`

    document.cookie = `${key}=;max-age=0;${_path}${_domain}`;
}

function cookieGet(
    key: string
) {
    var match = document.cookie.match(
        new RegExp(
            `${key}=(.+);?`
        )
    );

    if (match != null) return match[1];
    else return null;
}

function cookieSet(
    key: string,
    value: string,
    maxAge: number = null,
    expires: string = null,
    path: string = _path,
    domain: string = _domain
) {
    var _maxAge: string = "";
    if (maxAge != null) _maxAge = `max-age=${maxAge};`;

    var _expires: string = "";
    if (expires != null) _expires = `expires=${expires};`;

    var _path: string = "";
    if (path != null) _path = `path=${path};`

    var _domain: string = "";
    if (domain != null) _domain = `domain=${domain};`;

    document.cookie = `${key}=${encodeURIComponent(value)};${_maxAge}${_expires}${_path}${_domain}`;
}

// class cookie {
//     key: string;
//     value: string;
//     maxAge: number;
//     expires: string;
//     path: string;
//     domain: string;

//     constructor(
//         key: string,
//         value: string,
//         maxAge: number,
//         expires: string,
//         path: string,
//         domain: string
//     ) {
//         this.key = key;
//         this.value = value;
//         this.maxAge = maxAge;
//         this.expires = expires;
//         this.path = path;
//         this.domain = domain;
//     }

//     update() {
//         cookieSet(
//             this.key,
//             this.value,
//             this.maxAge,
//             this.expires,
//             this.path,
//             this.domain
//         );
//     }

//     updateValue(
//         value: string
//     ) {
//         this.value = value;

//         this.update();
//     }
// }

export { cookieRemove, cookieGet, cookieSet }