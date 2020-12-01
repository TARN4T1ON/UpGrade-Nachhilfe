const utc = "Thu, 01 Jan 1970 00:00:00 UTC";
function cookieRemove(key, path = "/") {
    var _path = "";
    if (path != null) {
        _path = `path=${path};`;
    }
    document.cookie = `${key}=;expires=${utc};${_path}`;
}
function cookieGet(key) {
    var match = document.cookie.match(new RegExp(`${key}=(.+);?`));
    if (match != null)
        return match[1];
    else
        return null;
}
function cookieSet(key, value, maxAge = null, expires = null, path = null, domain = null) {
    var _maxAge = "";
    if (maxAge != null)
        _maxAge = `max-age=${maxAge};`;
    var _expires = "";
    if (expires != null)
        _expires = `expires=${expires};`;
    var _path = "";
    if (path != null)
        _path = `path=${path};`;
    var _domain = "";
    if (domain != null)
        _domain = `domain=${domain};`;
    document.cookie = `${key}=${encodeURIComponent(value)};${_maxAge}${_expires}${_path}${_domain}`;
}
export { cookieRemove, cookieGet, cookieSet };
