const _path = "/";
const _domain = location.hostname;
function cookieRemove(key, path = _path, domain = _domain) {
    var _path = "";
    if (path != null)
        _path = `path=${path};`;
    var _domain = "";
    if (domain != null)
        _domain = `domain=${domain};`;
    document.cookie = `${key}=;max-age=0;${_path}${_domain}`;
}
function cookieGet(key) {
    var match = document.cookie.match(new RegExp(`${key}=(.+);?`));
    if (match != null)
        return match[1];
    else
        return null;
}
function cookieSet(key, value, maxAge = null, expires = null, path = _path, domain = _domain) {
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
